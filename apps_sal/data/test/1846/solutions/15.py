f = open('input.txt', 'r')
n = int(f.readline())
arr = list(map(int, f.readline().split()))

cntP = [0] * (n+1)
for i in range(1, n):
    cntP[i] = cntP[i-1] + (arr[i-1] >= 0)

cntN = [0] * (n+1)
for i in range(n-2, -1, -1):
    cntN[i] = cntN[i+1] + (arr[i+1] <= 0)

res = 2e9
for i in range(n-1):
    res = min(res, cntP[i+1] + cntN[i])
print(res, file = open('output.txt', 'w'))

