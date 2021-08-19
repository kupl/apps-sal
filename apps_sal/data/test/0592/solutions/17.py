n = int(input())
ans = 0
if(n == 2 or n == 3):
    print(0)
else:
    i = 2
    while(i <= n):
        j = 2
        num = n // i
        ans += (2 * num * (num + 1))
        ans -= 4
        i += 1
        # print(2*j*(j+1))
    print(ans)
