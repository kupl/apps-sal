q = int(input())
otvet = []
for i in range(q):
    g = input().split()
    n = int(g[0])
    m = int(g[1])
    k = int(g[2])
    if n < 0:
        n = -n
    if m < 0:
        m = -m
    if m > k or n > k:
        otvet.append(-1)
    elif m % 2 == k % 2 and n % 2 == k % 2:
        otvet.append(k)
    elif m % 2 == k % 2 or n % 2 == k % 2:
        otvet.append(k - 1)
    else:
        otvet.append(k - 2)
for i in otvet:
    print(i)
