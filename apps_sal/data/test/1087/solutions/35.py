N, K = map(int, input().split())

A = list(map(int, input().split()))
MAX = max(max(A), K)
l = len(str(bin(MAX))) - 2

AB = []
for i in range(N):
    s = str(bin(A[i]))
    temp = s[2:]
    lendif = l - len(temp)
    while lendif > 0:
        temp = "0" + temp
        lendif -= 1
    AB.append(temp)
# print(AB,l)

ans = 0
now = 0  # Kを超えていないかチェックする用。
for i in range(l):  # 桁数で回す。l-i桁から順にみていく。
    # cは0の数。dは1の数。
    c = 0
    d = 0
    for j in range(N):
        if AB[j][i] == "0":
            c += 1
        else:
            d += 1
    if c > d:  # 0の方が多いので1にしたい。l-i桁目が1の時はKを超えてないか確認。
        if pow(2, l - 1 - i) + now > K:
            m = d
        else:
            now += pow(2, l - 1 - i)
            m = c
    else:
        m = d
    #print(m, now, pow(2,l-1-i))
    ans += pow(2, l - 1 - i) * m
print(ans)
