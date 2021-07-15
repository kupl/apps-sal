def solve(n, a, b):
    l = (n+1)//2 - 1
    r = l + 1 + (n%2==0)
    lb = sum(sorted(a)[l:r])
    ub = sum(sorted(b)[l:r])
    return (ub - lb) + 1

n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
print(solve(n, a, b))
