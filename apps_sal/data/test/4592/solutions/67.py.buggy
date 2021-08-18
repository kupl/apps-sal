n = int(input())
if n == 1:
    print(1)
    return
l = [0] * (n + 1)  # 約数0~1000の各総数
for i in range(2, n + 1):
    x = i
    j = 2
    while j < n + 1:
        if x % j == 0:
            x //= j
            l[j] += 1
        else:
            j += 1
# print(l)
ans = 1
for i in range(len(l)):
    ans *= (l[i] + 1)
    ans %= (10**9 + 7)
print(ans)
