N = int(input())
S = list(input())

i = 1
count = 0
while i * 2 < N:
    n = 0
    while n + i * 2 < N:
        if (S[n] != S[n + i]) and (S[n + i] != S[n + 2 * i]) and (S[n] != S[n + i * 2]):
            count += 1
        n += 1
    i += 1

print(S.count('G') * S.count('R') * S.count('B') - count)
