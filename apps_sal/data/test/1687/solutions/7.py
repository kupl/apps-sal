n = int(input())
data = list(map(int, input().split()))
small = min(data)
for x in data:
    if x % small != 0:
        print(-1)
        import sys
        return
print(small)
