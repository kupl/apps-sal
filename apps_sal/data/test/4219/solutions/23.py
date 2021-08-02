#C - HonestOrUnkind2
N = int(input())
A = []
X = []
Y = []
for _ in range(N):
    a = int(input())
    A.append(a)
    box_x = []
    box_y = []
    for _ in range(a):
        x, y = map(int, input().split())
        box_x.append(x)
        box_y.append(y)
    X.append(box_x)
    Y.append(box_y)

person = [2] * N

maxim = 0
for i in range(1 << N):
    c_person = person.copy()
    honest = 0
    for j in range(N):
        mask = 1 << j
        if mask & i != 0:
            c_person[j] = 1
        else:
            c_person[j] = 0
    # 正直者かどうかの仮定
    for k, l in enumerate(c_person):
        # kが正直者のとき
        if l == 1:
            # kの証言を判定
            for m, n in zip(X[k], Y[k]):
                # 矛盾があるなら honest = 0でbreak
                if c_person[m - 1] != n:
                    honest = 0
                    break
            else:
                honest = sum(c_person)
                continue
            break
    maxim = max(maxim, honest)

print(maxim)
