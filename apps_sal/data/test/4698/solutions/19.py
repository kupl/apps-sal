n = int(input())
t = list(map(int, input().split()))
m = int(input())
p = [0 for _ in range(m)]
x = [0 for _ in range(m)]
for i in range(m):
    p[i], x[i] = map(int, input().split())

temp = sum(t)

for i in range(m):
    print(temp + (x[i] - t[p[i]-1]))
