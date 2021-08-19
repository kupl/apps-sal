(n, a) = list(map(int, input().split()))
ip = list(map(int, input().split()))
try:
    if a not in ip:
        ip.append(a)
        n += 1
    ip = sorted(ip)
    k = ip.index(a)
    l1 = 0
    l2 = 0
    for i in range(k):
        l1 += ip[i + 1] - ip[i]
    for i in range(k, n - 1):
        l2 += ip[i + 1] - ip[i]
    n1 = ip[1] - ip[0]
    n2 = ip[-1] - ip[-2]
    if l1 == 0:
        print(l2 - n2)
    elif l2 == 0:
        print(l1 - n1)
    else:
        print(min(l1 - n1 + 2 * l2, 2 * l1 - 2 * n1 + l2, l2 - n2 + 2 * l1, 2 * l2 - 2 * n2 + l1))
except:
    print(0)
