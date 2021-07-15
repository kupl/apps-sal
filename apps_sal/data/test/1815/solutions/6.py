n = int(input())
a = [int(x) for x in input().split()]
arr = [0] * 100001
freqs = [0] * 100001
freqs[0] = n
minf, maxf = 0, 0
for ind, i in enumerate(a):
    arr[i] += 1
    freqs[arr[i]] += 1
    freqs[arr[i] - 1] -= 1
    if not freqs[arr[i] - 1] and minf == arr[i] - 1:
        minf += 1
    maxf = max(maxf, arr[i])
    if maxf == 1 or (freqs[maxf] + freqs[0] == n - 1 and freqs[1] == 1) or (freqs[maxf] == 1 and freqs[maxf - 1] + freqs[0] == n - 1):
        best = ind + 1
print(best)

