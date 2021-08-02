import sys
# fin = open("ecr4a.in", "r")
fin = sys.stdin

n, p, q = map(int, fin.readline().split())
s = fin.readline().rstrip()


kp, kq = None, None
for i in range(0, n // p + 1):
    if not (n - i * p) % q:
        kp, kq = i, (n - i * p) // q
        break
else:
    print(-1)
    return

print(kp + kq)
cpos, m = 0, p * kp
while (cpos < m):
    print(s[cpos:cpos + p])
    cpos += p
while (cpos < n):
    print(s[cpos:cpos + q])
    cpos += q
