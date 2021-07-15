n = int(input())
a = list(map(int, input().split())) + [-1]
a.sort()
mx = 0
c = 0
cur = 0
for i in a:
    if i == c:
        cur += 1
    else:
        c = i
        cur = 1
    mx = max(mx, cur)
print(mx)

