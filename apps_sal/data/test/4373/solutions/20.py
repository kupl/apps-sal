n = int(input())
sp = list(map(int, input().split()))
sp.sort()
k = 1
ind = 0
while ind != n:
    if sp[ind] >= k:
        k += 1
    ind += 1
print(k - 1)
