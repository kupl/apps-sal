def fizzBuzzSum(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        if i % 3 != 0 and i % 5 != 0:
            sum += i
    return sum


n = int(input())
print(fizzBuzzSum(n))
