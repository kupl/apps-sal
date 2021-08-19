input()
(S, T) = map(str, input().split())
print(*[i + j for (i, j) in zip(S, T)], sep='')
