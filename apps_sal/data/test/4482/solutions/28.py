n = int(input())
A = list(map(int, input().split()))
ans = float('inf')
for x in range(-100, 101, 1):
    c = 0
    for a in A:
        c += (a - x) ** 2
    ans = min(c, ans)
print(ans)
