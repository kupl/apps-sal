route = list(map(int, input().split()))
route.sort()
print(sum(route[:2]))
