n, d = map(int, input().split())

area = (d*2)+1
if n%area == 0:
    ans = int(n//area)
else:
    ans = int(n//area) + 1

print(ans)
