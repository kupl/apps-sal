n = int(input())
a = [tuple(map(int, input().split())) for i in range(n)]
b = [tuple(map(int, input().split())) for i in range(n)]
x = min(a)
h = max(b)
print(x[0] + h[0], x[1] + h[1])
