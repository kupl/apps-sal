n = int(input())
answer = n // 3 * 2
n = n % 3
if n != 0:
    print(answer + 1)
else:
    print(answer)
