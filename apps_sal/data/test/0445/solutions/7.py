def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


n = int(input())
arr = list(map(int, input().split()))
count = {}
for i in arr:
    try:
        count[i] += 1
    except KeyError:
        count[i] = 1
numbers = list(count.keys())
numbers.sort()
(a, b) = (-1, -1)
flag = False
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if isPrime(numbers[i] + numbers[j]):
            a = numbers[i]
            b = numbers[j]
            flag = True
            break
    if flag:
        break
if a == b and a == -1:
    if numbers[0] == 1 and count[1] > 1:
        print(count[1])
        for i in range(count[1]):
            print(1, end=' ')
        print()
    else:
        print(1)
        print(numbers[0])
elif a == 1:
    print(count[1] + 1)
    for i in range(count[1]):
        print(1, end=' ')
    print(b)
elif numbers[0] == 1 and count[1] > 2:
    print(count[1])
    for i in range(count[1]):
        print(1, end=' ')
    print()
else:
    print(2)
    print(a, b)
