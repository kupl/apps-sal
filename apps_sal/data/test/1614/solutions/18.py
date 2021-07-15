3

n, h = list(map(int, input().split()))

a = list(map(int, input().split()))

ans = n

for i in range(n):
    if a[i] > h:
        ans += 1

print(ans)

