x, y = tuple(map(int, input().split()))
n = int(input())

answers = [x, y, y - x, -x, -y, -y + x]
print(answers[n % 6 - 1] % (10 ** 9 + 7))
