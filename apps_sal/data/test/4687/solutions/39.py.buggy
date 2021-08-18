n, k = map(int, input().split())
lst = [0] * 10**5
for i in range(n):
    a, b = map(int, input().split())
    lst[a - 1] += b
    ans = 0
for j in range(10**5):
    ans += lst[j]
    if ans >= k:
        print(j + 1)
        return
