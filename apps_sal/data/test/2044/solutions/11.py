n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
k = 0
ans = 0
for i in a:
    k += i
    ans = k // m
    k = k % m
    print(ans, end=" ")
