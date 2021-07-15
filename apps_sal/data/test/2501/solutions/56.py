n = int(input())
a = list(map(int, input().split()))
num = dict()
ans = 0

for i in range(n):
    num[i+a[i]] = 0

for i in range(n):
    if i-a[i] in num:
        ans += num[i-a[i]]
    num[i+a[i]] += 1
print(ans)
    

