# =__='

n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(input())

b = (n % 2 == 0)
while (b):
    b = True
    for i in range(n // 2):
        if (a[i] != a[n - i - 1]):
            b = False
            break
    
    b = b and (n % 2 == 0)
    if (b):
        n = n // 2

print(n)

