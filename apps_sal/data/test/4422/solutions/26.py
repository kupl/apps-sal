(N, K) = map(int, input().split())
K -= 1
S = list(input())
for (i, c) in enumerate(S):
    if i == K:
        c = c.lower()
    print(c, end='')
print('')
