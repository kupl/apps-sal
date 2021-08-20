from bisect import bisect_left
N = int(input())
L = list(map(int, input().split()))
L = sorted(L)
ans = 0
for i in range(N - 2):
    a = L[i]
    for j in range(i + 1, N - 1):
        b = L[j]
        '\n    lo=0\n    hi=N\n    x=a+b\n    while lo<hi:\n      mid=(lo+hi)//2\n      if L[mid]<x: lo=mid+1\n      else: hi=mid\n    ans+=lo-(j+1) \n    '
        ans += bisect_left(L, a + b) - (j + 1)
print(ans)
