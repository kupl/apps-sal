N, B, D = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 0
now = 0
for a in A:
    if a <= B:
        now += a
    if now > D:
        ans += 1
        now = 0
print(ans)

