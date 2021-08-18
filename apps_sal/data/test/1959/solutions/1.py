n, m = map(int, input().split())
a = list(map(int, input().split()))

counter = 0

s = set(a)
nech = set()
chet = set()
for elem in a:
    if elem % 2:
        nech.add(elem)
    else:
        chet.add(elem)

while len(nech) > n // 2:
    nech.pop()
while len(chet) > n // 2:
    chet.pop()

l_n = set([i for i in range(1, min(m + 1, 1000000), 2)])
l_ch = set([i for i in range(2, min(m + 1, 1000000), 2)])

l_ch.difference_update(chet)
l_n.difference_update(nech)


if len(l_ch) + len(chet) < n // 2 or len(l_n) + len(nech) < n // 2:
    print(-1)
else:
    n1 = len(chet)
    n2 = len(nech)
    for i in range(n):
        if a[i] in chet:
            chet.remove(a[i])
        elif a[i] in nech:
            nech.remove(a[i])
        else:
            counter += 1
            if (n // 2 - n1) > 0:
                a[i] = l_ch.pop()
                n1 += 1
            else:
                a[i] = l_n.pop()
                n2 += 1

    print(counter)
    print(*a)
