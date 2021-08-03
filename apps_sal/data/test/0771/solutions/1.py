n, k, m = map(int, input().split())
ip = list(map(int, input().split()))
arr = [[] for i in range(m)]
for i in ip:
    arr[i % m].append(i)
b = 0
for i in arr:
    if len(i) >= k:
        print('Yes')
        for j in i[:k]:
            print(j, end=' ')
        b = 1
        break
if b == 0:
    print('No')
