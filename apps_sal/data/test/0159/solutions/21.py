

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


n = int(input())

a = list(map(int, input().split()))


last = 1
ans = []

for i in range(n):
    if gcd(a[i], last) != 1:
        ans.append(1)
    ans.append(a[i])
    last = a[i]


print(len(ans) - n)

for i in range(len(ans) - 1):
    print(ans[i], end=' ')


print(ans[len(ans) - 1])
