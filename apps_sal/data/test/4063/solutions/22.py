N = int(input())
dlist = list(map(int, input().split()))
dlist.sort()
print(dlist[(N + 1) // 2] - dlist[(N - 1) // 2])
