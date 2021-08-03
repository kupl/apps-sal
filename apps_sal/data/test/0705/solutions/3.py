
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

s = set(x + y)

c = sum(xi ^ yj in s for xi in x for yj in y)
print('Koyomi' if c % 2 else 'Karen')
