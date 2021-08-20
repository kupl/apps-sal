x = input()
variants = [x] + [str(int(x[:i]) - 1) + '9' * (len(x) - i) for i in range(1, len(x))]
print(int(max(variants, key=lambda x: (sum(map(int, x)), int(x)))))
