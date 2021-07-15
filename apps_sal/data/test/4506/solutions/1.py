n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = []
for i in range(n):
    count.append((n-i)*(i+1)*a[i])
b.sort()
count.sort(reverse = True)
ans = 0
for i in range(n):

    ans += count[i]*b[i]
    ans %= 998244353
print(ans)

