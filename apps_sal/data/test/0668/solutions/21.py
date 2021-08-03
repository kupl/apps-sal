n = int(input())
k = list(map(int, input().split()))

if (k[0] == 0) or (sum(k) < (n - 1)):
    print(-1)
else:
    print(n - 1)
    l = [i + 1 for i in range(n) if k[i] != 0]
    k1 = [i for i in k if i != 0]
    ind = [i - 1 for i in l]
    m = [i + 1 for i in range(n) if k[i] == 0]

    for j in range(len(l) - 1):
        print(l[j], l[j + 1])
        k1[j] -= 1

    count = 0
    c = 0
    q = k1[0]

    while count < len(m):
        count += 1
        if q == 0:
            while q == 0:
                c += 1
                q = k1[c]
        print(ind[c] + 1, m[count - 1])
        q -= 1
