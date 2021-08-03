n, m = map(int, input().split())
K = list(map(int, input().split()))
l = L = len(K)
k = []
while L:
    L -= 1
    k.append([K[L], L + 1])
k.sort()
s = i = 0
while i < l:
    s += k[i][0]
    if s > m:
        s -= k[i][0]
        break
    i += 1
print(i)
while i:
    i -= 1
    if i:
        print(k[i][1], end=" ")
    else:
        print(k[i][1])
