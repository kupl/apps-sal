import sys
n = int(sys.stdin.readline())
sum = 0
for a7 in range(1, n - 11):
    if (n - a7) % 2 == 1:
        continue
    k = (n - a7) / 2 - 6
    res = (k + 5) * (k + 4) * (k + 3) * (k + 2) * (k + 1)
    res /= 120
    res %= 1000000007
    sum += res
    sum %= 1000000007
print(str(sum))
