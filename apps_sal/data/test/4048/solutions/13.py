def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = int(input())

yakusu_list = make_divisors(N)
if len(yakusu_list) % 2 == 1:
    ans = (yakusu_list[len(yakusu_list) // 2] - 1) * 2
else:
    ans = yakusu_list[len(yakusu_list) // 2 - 1] - 1 + yakusu_list[len(yakusu_list) // 2] - 1

print(ans)
