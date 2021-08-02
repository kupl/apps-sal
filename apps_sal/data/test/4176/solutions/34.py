A, B = list(map(int, input().split()))

i = 1
while True:
    n = A * i
    if n % B == 0:
        print(n)
        break
    i += 1
