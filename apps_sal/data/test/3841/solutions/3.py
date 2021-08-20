(p, k) = (int(x) for x in input().split())
rev_p_digits = []
p2 = p
curr_pow = 1
curr_k_pow = 1
i = 0
while p2 > 0:
    curr_pow += 1
    curr_k_pow *= k
    if curr_pow % 2 == 1:
        rev_p_digits.append((k - p2 % k) % k)
        p2 += rev_p_digits[-1]
    else:
        rev_p_digits.append(p2 % k)
    p2 //= k
print(len(rev_p_digits))
print(*rev_p_digits)
