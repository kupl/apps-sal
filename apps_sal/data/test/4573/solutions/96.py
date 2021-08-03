n = int(input())
x = list(map(int, input().split()))
y = sorted(x)
index = n // 2

for i in range(n):
    print(y[-index] if x[i] < y[index] else y[-index - 1])
