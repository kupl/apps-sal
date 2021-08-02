n = int(input())
result = int(n / 100)
n = n % 100
result += int(n / 20)
n = n % 20
if n >= 10:
    n -= 10
    result += 1
if n >= 5:
    n -= 5
    result += 1
result += n
print(result)
