n = int(input())

x = float('inf')
for _ in range(5):
    a = int(input())
    x = min(x,a)

print((n-1)//x + 5)
