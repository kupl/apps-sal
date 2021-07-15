import bisect
N = int(input())
L = list(map(int, input().split()))
count = 0

L.sort()

for i in range(N-2):
    for j in range(i+1,N-1):
        k = bisect.bisect_left(L,L[i]+L[j])
        count += k-j-1

print(count)
