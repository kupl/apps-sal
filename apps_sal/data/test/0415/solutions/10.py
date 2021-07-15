n = int(input())
ri = list(map(int,input().split()))
ar = [0] * (n+1)
ar[1] = ri[0]
for i in range(1,n):
    ar[i+1] = ar[i] + ri[i]
ans = 0
for i in range(n+1):
    for j in range(i+1,n+1):
        num = ar[j] - ar[i]
        num2 = j - i
        if num > num2 * 100:
            ans = max(ans,num2)
print(ans)

