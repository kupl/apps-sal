def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)  # remove odd numbers
    for n in range(int(limit**0.5 + 1.5)):  # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n * n, limit + 1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]


check = set(primes_upto(2 * 10**6 + 500))
n = int(input())
arr = list(map(int, input().split()))
one_present = False
cnt_ones = 0
for i in arr:
    if i == 1:
        one_present = True
        cnt_ones += 1

num1, num2, prime = 0, 0, 0
for i in range(n):
    for j in range(n):
        if one_present:
            if cnt_ones > 1:
                if arr[i] + arr[j] in check and arr[i] + 1 in check and arr[j] + 1 in check and arr[i] != 1 and arr[j] != 1:
                    num1 = arr[i]
                    num2 = arr[j]
                if arr[i] + 1 in check and arr[i] != 1:
                    num1 = arr[i]
                if arr[i] in check:
                    prime = arr[i]
            else:
                if arr[i] + arr[j] in check and arr[i] != 1 and arr[j] != 1:
                    num1 = arr[i]
                    num2 = arr[j]
                if arr[i] + 1 in check and arr[i] != 1:
                    num1 = arr[i]
                if arr[i] in check:
                    prime = arr[i]
        else:
            if arr[i] + arr[j] in check:
                num1 = arr[i]
                num2 = arr[j]
            if arr[i] in check:
                prime = arr[i]

if one_present:
    if cnt_ones > 1:
        if num2 == 0:
            if num1 == 0:
                print(cnt_ones)
                for i in range(cnt_ones):
                    print(1, end=' ')
            else:
                print(cnt_ones + 1)
                for i in range(cnt_ones):
                    print(1, end=' ')
                print(num1, end=' ')
        else:
            print(cnt_ones + 2)
            for i in range(cnt_ones):
                print(i, end=' ')
            print(num1, end=' ')
            print(num2, end=' ')
    else:
        if num2 == 0:
            if num1 == 0:
                print(1)
                print(1)
            else:
                print(2)
                print('1 ' + str(num1))
        else:
            print(2)
            print(str(num1) + ' ' + str(num2))
else:
    if num1 == 0:
        if prime == 0:
            print(1)
            print(arr[0])
        else:
            print(1)
            print(prime)
    else:
        print(2)
        print(str(num1) + ' ' + str(num2))
