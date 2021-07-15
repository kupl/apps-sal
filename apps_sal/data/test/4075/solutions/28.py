from itertools import product
n,m = list(map(int, input().split()))
S = []
for _ in range(m):
    k, *s = list(map(int, input().split()))
    S.append(s)
p = list(map(int, input().split()))

ans = 0
for pattern in product(range(2), repeat=n):
    # 電球がつくかチェック
    for x,y in zip(S, p):
        on_cnt = sum([pattern[s-1] == 1 for s in x])
        if on_cnt % 2 != y:
            break
    else:
        ans += 1

print(ans)
