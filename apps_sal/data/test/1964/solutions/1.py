n = int(input())
k = [int(i) for i in input().split()]
m = []
for i in range(n):
    m.append([int(j) for j in input().split()])
t = [0] * n
for i in range(n):
    t[i] = sum(m[i]) * 5 + len(m[i]) * 15
print(min(t))
