m = int(input())
a = list(map(int, input().split()))
n = int(input())
b = list(map(int, input().split()))
if(sum(a) != sum(b)):
    print(-1)
else:
    ans = sum1 = sum2 = 0
    i = j = 0
    while(i < m and j < n):
        if(sum1 < sum2):
            sum1 += a[i]
            i += 1
        elif(sum1 > sum2):
            sum2 += b[j]
            j += 1
        else:
            ans += 1
            sum1 = a[i]
            sum2 = b[j]
            i += 1
            j += 1
    print(ans)
