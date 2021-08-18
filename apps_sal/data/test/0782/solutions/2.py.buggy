m = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return (a)
    return (gcd(b, a % b))


cur = min(a)
for i in range(1, m):
    if a[i] % cur != 0:
        print("-1")
        return
L = [cur]

for i in range(m):
    if a[i] != cur:
        L.append(a[i])
        L.append(cur)

print(len(L))

for i in range(len(L)):
    print(L[i], end=' ')
