(a, b) = list(map(int, input().split()))
if b - a >= 5:
    print('0')
else:
    num_term = b - a
    num = 1
    for i in range(num_term):
        num = num * ((a + i + 1) % 10)
        num = num % 10
    print(num)
