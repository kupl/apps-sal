x = int(input())
s = [int(i) for i in input().split()]
n = min(s)
count = n * x
t = 0
for i in range(x):
    s[i] -= n
s += s
m = 0
for i in s:
    if not i:
        m = max(m, t)
        t = 0
    else:
        t += 1
print(count + m)
