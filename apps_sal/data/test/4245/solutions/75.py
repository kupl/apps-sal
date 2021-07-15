a,b = map(int,input().split())
ans = 1
i = 0
if b != 1:
    while ans <b:
        i += 1
        ans = a + (a-1)*(i-1)

print(i)
