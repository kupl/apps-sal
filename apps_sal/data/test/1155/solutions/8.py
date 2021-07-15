n, m = [int(i) for i in input().split()]

ans = 100000.0

for i in range(n):
    a, b = [int(i) for i in input().split()]
    x = m * (a / b)
    if x < ans:
        ans = x
        
print(ans)
