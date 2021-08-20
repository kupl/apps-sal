def is_palindrome(num):
    copia = num
    if num < 10:
        return True
    nums = []
    while True:
        nums.append(copia % 10)
        copia //= 10
        if copia == 0:
            break
    digitos = len(nums) // 2
    j = len(nums) - 1
    for i in range(digitos):
        if nums[i] != nums[j]:
            return False
        j -= 1
    return True


primes = [True] * 2000000
primes[0] = False
num = input().split()
num = [int(num[0]), int(num[1])]
resultado = 0
i = 0
countPrimes = 0
countPali = 0
while i < 2000000:
    if primes[i]:
        countPrimes += 1
        if i * i < 2000000:
            for j in range(i, 2000000, i + 1):
                primes[j] = False
    if str(int(str(i + 1)[::-1])) == str(i + 1):
        countPali += 1
    res = countPali * num[0] / num[1]
    if res >= countPrimes:
        resultado = i + 1
    i += 1
if resultado == 0:
    print('Palindromic tree is better than splay tree')
else:
    print(resultado)
