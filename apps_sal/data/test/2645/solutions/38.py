S = input()
N = len(S)
print(N // 2 - sum([int(s == 'p') for s in S]))
