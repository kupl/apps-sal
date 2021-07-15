n = int(input())
v = [int(n) for n in input().split()]

v = sorted(v)

ans = v[0]
for num in v[1:]:
    ans = (ans + num)/2

print(ans)
