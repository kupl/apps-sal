n = int(input())
m = int(input())
l = [0 for i in range(n)]
for i in range(n):
    l[i] = int(input())
d1 = max(l)
d2 = min(l)
e = sum(l)
r = (e + m)
if (r % n == 0):
    r1 = r // n
else:
    r1 = r // n + 1
print(max(d1, r1), d1 + m)
