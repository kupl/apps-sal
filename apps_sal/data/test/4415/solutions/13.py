from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

C = Counter(arr)
flag = 0

for keys in C:
    if C[keys]>=3:
        flag = 1
        print("NO")
        break

if flag==0:
    print("YES")
    es = []
    ds = []
    for keys in C:
        if C[keys]==2:
            es.append(keys)
            ds.append(keys)
        else:
            es.append(keys)

    es.sort()
    ds.sort()
    ds = ds[::-1]

    print(len(es))
    print(*es)
    print(len(ds))
    print(*ds)

