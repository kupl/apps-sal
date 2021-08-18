import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))


ans = []
plusmax = 0
minusmax = 0
plusmax_i = -1
minusmax_i = -1

target = -1
maxdiff = 0
for i in range(len(A)):
    if A[i] < minusmax:
        minusmax = A[i]
        minusmax_i = i
    if A[i] > plusmax:
        plusmax = A[i]
        plusmax_i = i

if abs(plusmax) > abs(minusmax):
    maxval = plusmax
    max_i = plusmax_i
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:
            ans.append((max_i + 1, i + 1))
            ans.append((max_i + 1, i + 1))
            A[i] += 2 * maxval
            max_i = i
            maxval = A[i]
else:
    minval = minusmax
    min_i = minusmax_i
    for i in range(len(A) - 1, 0, -1):
        if A[i - 1] > A[i]:
            ans.append((min_i + 1, i))
            ans.append((min_i + 1, i))
            A[i - 1] += 2 * minval
            min_i = i - 1
            minval = A[i - 1]

print((len(ans)))
for a in ans:
    print((*a))
