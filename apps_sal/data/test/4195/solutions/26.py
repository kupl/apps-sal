(D, N) = map(int, input().split())
count = 0
i = 1
while count < N:
    if i % 100 ** (D + 1) != 0 and i % 100 ** (D + 2) != 0 and (i % 100 ** D == 0):
        count += 1
    i += 1
print(i - 1)
