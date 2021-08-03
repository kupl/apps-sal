n = int(input())
div_map = dict()
mod = 10 ** 9 + 7

for i in range(1, n + 1):
    is_prime_number = True
    for j in range(2, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            is_prime_number = False
            break
    if is_prime_number:
        if i not in div_map:
            div_map[i] = 1
        else:
            div_map[i] += 1
    else:
        j = 2
        while i != 1:
            if i % j == 0:
                if j not in div_map:
                    div_map[j] = 1
                else:
                    div_map[j] += 1
                i //= j
            else:
                j += 1


res = 1
div_map[1] = 0
for key, value in list(div_map.items()):
    res = res * (value + 1) % mod

print((res % mod))
