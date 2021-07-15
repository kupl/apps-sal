n = int(input())
prime_lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
lst = [0 for _ in range(n)]
for i in range(1, n + 1):
    a = i
    for num in prime_lst:
        while a % num == 0:
            lst[num - 1] += 1
            a //= num
    if a != 1:
        lst[a - 1] += 1
ans = 1
MOD = 10 ** 9 + 7
for num in lst:
    ans *= (num + 1)
    ans %= MOD
print(ans)
