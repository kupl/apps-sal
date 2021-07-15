# 方針は解説と全く同じなので割愛

n = int(input())

# 約数列挙
# ABC136Eより
def get_divisors(num):
    if num == 1:
        return [1]
    
    divisors = []
    for d in range(1, num):
        if d * d > num:
            break
        if num % d == 0: #約数
            divisors.append(d)
            if d * d != num:  # numの平方根の場合は重複するので追加しない
                divisors.append(int(num // d))

    return divisors


ans = len(get_divisors(n-1)) - 1

for divisor in get_divisors(n):
    if divisor == 1:
        continue
    temp = n
    while(True):
        if temp % divisor != 0:
            break
        temp = temp // divisor
    
    if temp % divisor == 1:
        ans += 1

print(ans)

