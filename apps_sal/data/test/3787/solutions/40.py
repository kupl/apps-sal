n,a,b = map(int,input().split())
turn = 0
if b > a:
    turn = 1
    a,b = b,a
x = (n+a-1)//a
if x > b or a+b > n+1:
    print(-1)
    return

ans = []
m = n%a
now = n
while x < b:
    ans.append(now)
    now -= 1
    if m:
        m -= 1
        x += 1
    else:
        m = a-1
for i in range((now+a-1)//a):
    for j in range(a-1,-1,-1):
        num = now-i*a-j
        if num > 0:
            ans.append(num)
if turn:
    ans = ans[::-1]
print(*ans)
