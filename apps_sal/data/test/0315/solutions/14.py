n,k = map(int, input().split())
num = list(map(int, input().split()))

ans = 0

for i in range(1,n):
    if num[i]+num[i-1]<k:
        ans += k-(num[i]+num[i-1])
        num[i] = k-num[i-1]

print(ans)
print(' '.join([str(x) for x in num]))
