from functools import reduce
n = int(input())
a = list(map(int, input().split()))
print(max([reduce(int.__xor__, a[i:j]) for j in range(1, n + 1) for i in range(j)]))
