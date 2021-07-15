import sys, bisect

N = int(input())
L = list(map(int, sys.stdin.readline().rsplit()))
L.sort()

res = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        a, b = L[i], L[j]
        c_l = bisect.bisect_left(L, a + b)
        
        if c_l <= j:
            continue
        
        # print(i, j, c_l)
        res += c_l - (j + 1)

print(res)

