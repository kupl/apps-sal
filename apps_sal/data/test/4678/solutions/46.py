n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(len(a) - 1):
         if a[i+1] < a[i]:
                  ans += a[i] - a[i+1]
                  a[i+1] = a[i]
print(ans)


