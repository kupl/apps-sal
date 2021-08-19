N = input()
S = sum(map(int, list(N)))
print('Yes' if int(N) % S == 0 else 'No')
