n = int(input())
sz = list(map(int, input().split()))
max_sz = max(sz)
print(2 * max_sz - sum(sz) + 1)
