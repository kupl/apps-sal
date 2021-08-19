N = int(input())
s = 2
t = 1
for i in range(0, N):
    u = s + t
    (s, t, u) = (t, u, s)
print(s)
