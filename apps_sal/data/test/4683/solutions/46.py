n = int(input())
a = list(map(int, input().split()))

suma = sum(a)
ans = 0
for i in range(len(a)):
    suma = suma - a[i]
    ans += suma * a[i]
ans = ans % (10**9 + 7)
print(ans)
