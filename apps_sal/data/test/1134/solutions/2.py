n = int(input())
m = input().split()
t = []
for i in range(n):
    m[i] = int(m[i])
    if i == 0:
        t.append(m[i]+1)
    else:
        t.append(max(t[i-1], m[i]+1))
s = t[n-1] - m[n-1] - 1
for i in range(n-2, -1, -1):
    if t[i] < t[i+1]-1:
        t[i] = t[i+1]-1
    s += t[i] - m[i] - 1
print(s)
