n = int(input())
v = list(map(int, input().split()))

v.sort()
for x in v:
    if(x % v[0] != 0):
        print(-1)
        return

print(v[0])






