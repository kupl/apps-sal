S = input(); print(sum(a != b for a, b in zip(S, S[::-1])) // 2)
