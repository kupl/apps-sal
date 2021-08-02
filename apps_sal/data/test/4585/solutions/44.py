N = int(input())
for i in range(1, N // 2 + 10):
    tmp = ((i + 1) * (i)) // 2
    if N - tmp == 0:
        print(i)
        return
    if N - tmp < i + 1:
        print(i + 1)
        return
