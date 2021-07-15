n,x = map(int,input().split())
ans = 0
i = n
while i >= 0:
    c = 2**(i+1) - 3
    num_p = 2**i - 1
    
    if 2*c + 3 == x:
        ans += 2*num_p + 1
        break
    elif c + 2 == x:
        ans += num_p + 1
        break
    elif 1 == x:
        break
    
    elif 2 + c <= x:
        x -= 2 + c
        ans += num_p + 1
    else:
        x -= 1
    
    i -= 1

print(ans)
