def make_prime_numbers(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False
    prime_numbers = [i for i in range(n + 1) if is_prime[i]]
    return prime_numbers


n = int(input())
prime_list = make_prime_numbers(n)
ans = [0] * (n + 1)
for (i, num) in enumerate(prime_list):
    tmp_num = num
    while tmp_num < n + 1:
        ans[tmp_num] = i + 1
        tmp_num += num
print(' '.join(map(str, ans[2:])))
