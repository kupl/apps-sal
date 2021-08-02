
N = int(input())

num = N - 1

if num <= 3 or num % 2 == 1:
    print('NO')
    quit()

x = 1

y = (num - 2) // 2

print(x, y)
