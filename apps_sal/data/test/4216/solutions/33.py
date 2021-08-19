N = int(input())
M = 1
for i in range(1, int(N ** (1 / 2)) + 1):
    if N % i == 0:
        if M < i:
            M = i
M = N // M
ndm = len(list(str(M)))
print(ndm)
