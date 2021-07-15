n = int(input())
sp = []
for i in range(n):
    sp.append(int(input()))
sp.sort()
s = 0
for i in range(n):
    s = (s + sp[i] * sp[-i-1]) % 10007
print(s)

