N = int(input())
p = []
for i in range(N):
    p.append(int(input()))
a = max(p)
p.remove(a)
s = 0
for i in p:
    s += i
print(s + a // 2)
