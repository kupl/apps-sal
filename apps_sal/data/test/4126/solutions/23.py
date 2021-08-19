S = input()
l = len(S) // 2
print('YNeos'[any(map(lambda s: any((c != d for (c, d) in zip(s, s[::-1]))), [S, S[:l], S[-l:]]))::2])
