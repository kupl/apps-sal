mod = 10**9 + 7
n = int(input())
l = list(map(int, input().split()))
sum_l = sum(l)
ans = 0
for i in range(n):
    sum_l -= l[i]
    ans += sum_l * l[i]
print(ans % mod)
