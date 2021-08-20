n = int(input())
thing = input().split(' ')
l = []
for i in range(n):
    l.append(int(thing[i]))
m = [-1] * n
for i in range(n):
    m[l[i] - 1] = i
t = 0
for i in range(n - 1):
    t += abs(m[i] - m[i + 1])
print(t)
