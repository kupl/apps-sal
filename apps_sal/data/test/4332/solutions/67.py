def sum_digit(n):
    temp = 0
    while n > 0:
        temp += n % 10
        n //= 10
    return temp


n = int(input())
print('Yes' if n % sum_digit(n) == 0 else 'No')
