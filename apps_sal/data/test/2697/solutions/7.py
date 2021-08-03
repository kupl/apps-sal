def count_Primes_nums(n):
    ctr = 0

    for num in range(n + 1):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr


try:
    n = int(input())
    print(count_Primes_nums(n))
except:
    pass
