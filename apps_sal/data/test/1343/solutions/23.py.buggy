mat = []
pek = set()

n, m, k = list(map(int, input().split()))
arr = []
for i in range(m):
    u, v, l = list(map(int, input().split()))
    arr.append([l, u, v])
if k:
    pek = set(map(int, input().split()))
    arr.sort()
    for i in range(m):
        if arr[i][1] in pek and arr[i][2] not in pek:
            print(arr[i][0])
            return
        if arr[i][2] in pek and arr[i][1] not in pek:
            print(arr[i][0])
            return
    print(-1)
else:
    print(-1)
