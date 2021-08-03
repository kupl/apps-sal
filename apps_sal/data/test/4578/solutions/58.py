n, x = map(int, input().split())
m = [int(input()) for i in range(n)]
m.sort()
temp = 0
for g in m:
    temp += g
print((x - temp) // m[0] + len(m))
