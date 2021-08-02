n, m = map(int, input().split())
ans = 0
if(m % n == 0):
    m //= n
else:
    m = 1
    ans = -1
while(m != 1):
    if(m % 2 == 0):
        m //= 2
        ans += 1
    elif(m % 3 == 0):
        m //= 3
        ans += 1
    else:
        ans = -1
        break
print(ans)
