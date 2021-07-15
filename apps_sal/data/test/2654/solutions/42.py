a = []
b = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
a.sort()
b.sort()
if n % 2 == 1:
    print(b[(n-1)//2] - a[(n-1)//2]+1)
    return
print(b[n//2] + b[n//2-1] - a[n//2] - a[n//2-1] + 1)
