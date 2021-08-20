t = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = []
u = 0
for i in range(0, t):
    if x[i] >= u:
        print(i, end=' ')
        u = y[i]
