n = int(input())
total = 2 * n - 2
if n == 3:
    print(24)
else:
    free = total - n - 2 + 1
    ans = 0
    ans += 4 * 2 * 3 * pow(4, total - n - 1)
    left = 2
   # print(total-n+1)
    while left < total - n + 1:
        # print(left)
        ans += 4 * 3 * 3 * pow(4, left - 2) * pow(4, total - left - n)
       # print(str(left-2)+' '+str(total-left-n))
        left += 1
    print(ans)
