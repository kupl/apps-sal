n = int(input())
s = int(input())
if n == s:
    print(n + 1)
    return

m = abs(n-s)

a = set()
i = 1
while i * i <= m:
    if m % i == 0:
        a.add(i)
        a.add(m // i)
    i += 1

for i in sorted(list(a)):
    i += 1
    su = 0
    nn = n
    while nn:
        su += nn % i
        nn //= i
    if su == s:
        print(i)
        break
else:
    print(-1)
