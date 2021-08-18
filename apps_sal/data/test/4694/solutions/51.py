homecnt = int(input())
homeplace = list(map(int, input().split()))

dist = max(homeplace) - min(homeplace)
print(dist)
