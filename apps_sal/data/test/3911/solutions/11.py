def get(k):
    find = False
    for i in range(len(k)):
        if k[i] == 0:
            k[i] = 1
            break
        else:
            k[i] = 0
    else:
        k.append(1)
    return k


n = int(input())
k = []
for i in range(n):
    k = get(k)
for i in range(len(k) - 1, -1, -1):
    if k[i]:
        print(i + 1, end=' ')
