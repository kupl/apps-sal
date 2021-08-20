N = int(input())
(S, T) = list(map(str, input().split()))
i = 0
ST = ''
while i < N:
    ST = ST + S[i] + T[i]
    i += 1
print(ST)
