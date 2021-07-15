N = int(input())
a = list(map(int,input().split()))
s = list(sorted(a))
ind = {}
for i in range(N):
    if s[i] not in ind:
        ind[s[i]] = i
for i in range(N):
    if ind[a[i]] < N//2:
        print(s[N//2])
    else:
        print(s[N//2-1])
