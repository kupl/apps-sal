m, n = list(map(int, input().split()))
L = []
for i in range(0, m):
    s = [int(x) for x in input().split()]
    s = s[1:]
    L.append(set(s))

for i in range(m - 1):
    for j in range(i + 1, m):
        if(len(L[i] & L[j]) == 0):
            print('impossible')
            break
    else:
        continue
    break
else:
    print('possible')
