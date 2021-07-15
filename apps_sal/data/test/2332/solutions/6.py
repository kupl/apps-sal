n, k, m = map(int, input().split())
arr = list(map(str, input().split()))
d = dict()
for i in range(n):
    d[arr[i]] = i
coin = list(map(int, input().split()))
coin2 = [0 for i in range(n)]
for i in range(k):
    mass = list(map(int, input().split()))
    mass2 = []
    for j in range(1, len(mass)):
        mass2.append(mass[j] - 1)
    mi = coin[mass2[0]]
    for j in range(len(mass2)):
        if(mi > coin[mass2[j]]):
            mi = coin[mass2[j]]
    for j in range(len(mass2)):
        coin2[mass2[j]] = mi
arr2 = list(map(str, input().split()))
ans = 0
for i in range(m):
    ind = d[arr2[i]]
    ans += coin2[ind]
print(ans)
