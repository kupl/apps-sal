n, r = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

enabled = [0]*n
ans = 0
i = 0
breaked = False
while i < n:
    j = i + r - 1
    
    heater = -1
    while j >= i-r+1:
        if j>=0 and j < n and a[j] == 1:
            heater = j
            break
        j -= 1
    #print(heater)
    if heater == -1:
        breaked = True
        break
    else:
        i = heater + r
    ans += 1
    
if not breaked:
    print(ans)
else:
    print(-1)

