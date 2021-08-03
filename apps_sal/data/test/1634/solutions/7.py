c1, c2, c3, c4 = map(int, input().split())
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = []
s0 = 0
for i in range(n):
    s.append(min(a[i] * c1, c2))
    s0 += s[i]
s1 = []
s10 = 0
for i in range(m):
    s1.append(min(b[i] * c1, c2))
    s10 += s1[i]
print(min((min(s0, c3) + min(s10, c3)), c4))
