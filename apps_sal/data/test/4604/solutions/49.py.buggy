n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7

a.sort()

if n % 2 == 1:
    if a[0] != 0:
        print((0))
        return
    else:
        a.remove(0)
        tmp = 2
else:
    tmp = 1

for i in range(n // 2):
    if tmp == a[0] and tmp == a[1]:
        a.remove(tmp)
        a.remove(tmp)
    else:
        print((0))
        return
    tmp += 2

if len(a) == 0:
    print(((2**(n // 2)) % mod))
else:
    print((0))
