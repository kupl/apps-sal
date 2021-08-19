(n, m, k) = list(map(int, input().split()))
an = [0] + list(map(int, input().split()))
na = [0] * (n + 1)
bm = list(map(int, input().split()))
num = 0
for i in range(1, n + 1):
    na[an[i]] = i
for i in range(m):
    if na[bm[i]] != 1:
        temp = an[na[bm[i]] - 1]
        an[na[bm[i]] - 1] = an[na[bm[i]]]
        an[na[bm[i]]] = temp
        num += (na[bm[i]] - 1) // k
        temp2 = na[bm[i]]
        na[bm[i]] = na[temp]
        na[temp] = temp2
print(num + m)
