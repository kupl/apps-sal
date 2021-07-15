ans = 0
a, b = list(map(int, input().split()))
l = 2
pos = l-2
ans = 0
while True:
    n = ((1 << l) - 1) - (1 << pos)
    #print(l, pos, n)
    if n > b:
        break
    if n >= a:
        ans += 1
    if pos > 0:
        pos -= 1
    else:
        l += 1
        pos = l-2
print(ans)
    

