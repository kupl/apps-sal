n = int(input())
for kase in range(n):
    c, sum = [int(x) for x in input().split()]
    x = sum // c
    y = sum % c
    ans = (x + 1) * (x + 1) * y + (x * x) * (c - y)
    print(ans)
