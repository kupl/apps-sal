(n, k) = list(map(int, input().split()))
s = input()
p = []
q = []
x = input().split()
k = ''
t = 0
for i in s:
    if i in x:
        k += i
        t += 1
    else:
        p.append(k)
        q.append(t)
        k = ''
        t = 0
p.append(k)
q.append(t)
res = 0
for i in q:
    res += i * (i + 1) // 2
print(res)
