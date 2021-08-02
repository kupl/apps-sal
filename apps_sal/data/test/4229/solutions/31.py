print(sum([i, 0][i % 3 == 0 or i % 5 == 0] for i in range(1, int(input()) + 1)))
