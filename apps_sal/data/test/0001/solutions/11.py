def sum_div(n):
    summa = 0
    while n > 0:
        summa = summa + n % 10
        n = n // 10
    return summa


def run(n):
    l_n = len(n)
    left = ''
    if l_n > 2 and '9' * l_n != n and n[1] == '9' and '9' * (l_n - 1) != n[1:]:
        left = n[0]
        n = n[1:]
        while l_n > 1 and n[1] == '9':
            left += n[1]
            n = n[1:]
            l_n = len(n)
    l_n = len(n)
    if len(n) == 1:
        return n
    elif '9' * (l_n - 1) == n[1:]:
        return left + n
    elif n[0] != '1':
        min_number = int(str(int(n[0]) - 1) + '9' * (l_n - 1))
        if sum_div(min_number) > sum_div(int(n)):
            return left + str(min_number)
        else:
            return left + n
    else:
        min_number = int('9' * (l_n - 1)) if l_n > 1 else 0
        if sum_div(min_number) > sum_div(int(n)):
            return left + str(min_number)
        else:
            return left + n


n = input()
print(run(n))
