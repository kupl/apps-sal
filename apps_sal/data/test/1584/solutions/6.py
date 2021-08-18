import bisect

N = int(input())
L = sorted([int(n) for n in input().split()])

count = 0
for i in range(N - 1):
    b = L[:i]
    c = L[i + 1:]
    for j in b:
        count += bisect.bisect_left(c, L[i] + j)

print(count)
