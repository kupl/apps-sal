N, M = map(int, input().split())
abs_NM = abs(N - M)
if abs_NM > 1:
    print(0)
    return

p = 10**9 + 7
min_ = min(N, M)
max_ = max(N, M)
ans = 1
for i in range(1, min_ + 1):
    ans = (ans * i) % p
    ans = (ans * i) % p

if abs_NM == 1:
    ans = (ans * max_) % p
else:
    ans = (ans * 2) % p

print(ans)
