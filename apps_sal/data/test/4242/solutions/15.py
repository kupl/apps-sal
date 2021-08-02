a, b, k = list(map(int, input().split()))
n = max(a, b)
numlist = []
for i in range(1, n + 1):
    if a % i == b % i == 0:
        numlist.append(i)
numlist.sort(reverse=True)
print((numlist[k - 1]))
