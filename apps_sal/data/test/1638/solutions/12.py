n = int(input())
m = list(map(int, input().split()))
ans = []
totalmax = 0
for top in range(n):
    lst = [0] * n
    lst[top] = m[top]
    for i in range(top - 1, -1, -1):
        lst[i] = min(lst[i + 1], m[i])
    for i in range(top + 1, n):
        lst[i] = min(lst[i - 1], m[i])
    total = sum(lst)
    if totalmax < total:
        ans = lst
        totalmax = total

print(*ans, sep=" ")
