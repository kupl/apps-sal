(n, m) = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
D2 = {}
T = {}
ans = ''
for i in L:
    if i in D2:
        D2[i] += 1
    else:
        D2[i] = 1
    if D2[i] in T:
        T[D2[i]].append(i)
    else:
        T[D2[i]] = [i]
    if len(T[D2[i]]) % n == 0:
        ans = ans + '1'
    else:
        ans = ans + '0'
print(ans)
