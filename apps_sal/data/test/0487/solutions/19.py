from math import ceil
n = int(input())
votes = list(map(int, input().strip().split()))
sumv = sum(votes)
print(max(1 + 2 * sumv // n, max(votes)))
