N, K = map(int, input().split())
print(sum([h >= K for h in map(int, input().split())]))
