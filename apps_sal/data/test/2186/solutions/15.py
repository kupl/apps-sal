M = 9999999999879998


def myhash(target):
    h = 0
    p = 1
    for j in target:
        h = (h + p * ord(j)) % M
        p = (p * 197) % M
    return h


def binarysearch(base, tar):
    low = 0
    high = len(base) - 1
    while low <= high:
        mid = (low + high) // 2
        midval = base[mid]
        if midval > tar:
            high = mid - 1
        elif midval < tar:
            low = mid + 1
        else:
            return 1
    return 0


n, m = [int(i) for i in input().split()]
hashval = list()
ans = list()
for i in range(n):
    ini = input()
    h = myhash(ini)
    p = 1
    for j in range(len(ini)):
        for k in range(97, 100):
            if ini[j] != chr(k):
                hashval.append((h + p * (k - ord(ini[j]))) % M)
        p = (p * 197) % M
hashval.sort()

for i in range(m):
    query = input()
    hashtem = myhash(query)
    if binarysearch(hashval, hashtem):
        ans.append('YES')
    else:
        ans.append('NO')

print('\n'.join(ans))
