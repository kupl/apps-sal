
_ = int(input())
A = sorted(list(map(int, input().split())))[::-1]

ans = 0
for i, a in enumerate(A):
    if i % 2 == 0:
        ans += a
    else:
        ans -= a

print(ans)
