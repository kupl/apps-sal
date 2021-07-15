n = int(input())
ans = 0
for i in range(1,n+1):
    if i % 3 == 0:
        ans = ans
    elif i % 5 == 0:
        ans = ans
    else:
        ans += i
print(ans)
