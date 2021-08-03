def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1
u = [False] * n
ans = 1
for i in range(n):
    if (u[i] == False):
        x = i
        c = 1
        while (True):
            u[x] = True
            if (a[x] == i):
                break
            if (u[a[x]] != False):
                print(-1)
                return
            x = a[x]
            c += 1
        if (c % 2 == 0):
            c //= 2
        ans = ans * c // gcd(ans, c)
print(ans)
