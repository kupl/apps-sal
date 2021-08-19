n = int(input())
h = list(map(int, input().split()))
tmp = [0 for i in range(n)]
ans = 0
right = 0
left = n - 1
while tmp != h:
    for i in range(n):
        if tmp[i] != h[i]:
            right = i
            left = i
            break
    for i in range(i + 1, n):
        if tmp[i] == h[i]:
            left = i - 1
            break
        elif i == n - 1 and tmp[n - 1] != h[n - 1]:
            left = n - 1
            break
    for i in range(right, left + 1):
        tmp[i] += 1
    ans += 1
print(ans)
