print(sum((i - j < i ^ j < j for i in range(int(input()) + 1) for j in range(i // 2, i))))
