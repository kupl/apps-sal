def cal(N):
    num = (N**0.5) // 1
    num = int(num)
    for i in range(num, 0, -1):
        if N % i == 0:
            k = int(N / i)
            x = len(str(k))
            break
    return x


print(cal(int(input())))
