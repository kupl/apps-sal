mx = 2000000000

l, r = map(int, input().split())
ans = 0
arr = []
k = 1
while k <= mx:
    c = k
    while c <= mx:
        arr.append(c)
        c = 3 * c
    k = 2 * k

for x in arr:
    if x >= l and x <= r:
        ans = ans + 1

print(ans)
