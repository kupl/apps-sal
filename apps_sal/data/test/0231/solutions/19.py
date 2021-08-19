[n, x] = list(map(int, input().split(' ')))
answer = int(x % 2 == 0 and n / 2 - x / 2 + 1 or (x + 1) / 2)
print(answer)
