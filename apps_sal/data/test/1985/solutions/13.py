from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))


k, n = rint()

a = list(rint())
b = list(rint())

for i in range(1, k):
    a[i] = a[i] + a[i - 1]

a0 = min(a)
for i in range(len(a)):
    a[i] -= a0
a = set(a)

b0 = min(b)
for i in range(n):
    b[i] -= b0

ans = 0
for aa in a:
    diff = aa
    ans += 1
    for bb in b:
        if bb + diff in a:
            pass
        else:
            ans -= 1
            break

print(ans)
