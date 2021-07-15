a,b,c,d = list(map(int,input().split()))

a,b,c = sorted([a,b,c])

dist = 0
dist += max(0, d - (b-a))
dist += max(0, d - (c-b))

print(dist)

