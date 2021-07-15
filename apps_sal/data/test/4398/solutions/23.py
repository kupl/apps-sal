input()
S, T = input().split()
print(*[i + j for i, j in zip(S, T)], sep='')
