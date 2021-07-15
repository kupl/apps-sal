n = int(input())
a = list(map(int,input().split()))
tl = [0 for i in range(n)]
for i in range(n):
    tl[a[i] -1] = str(i+1)
print(' '.join(tl))
