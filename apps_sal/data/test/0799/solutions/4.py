n = int(input())
v = list(map(int, input().split()))
mx = max(v)
v = [mx - x for x in v]
print(sum(v))
