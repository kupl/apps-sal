from collections import defaultdict
t = int(input())
for _ in range(t):
    a, b, c = [int(x) for x in input().split()]
    print(max(a, b, c) + 1)
