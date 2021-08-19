N = list(map(int, input()))
N = N[::-1] + [0]
count = 0
for (i, n) in enumerate(N):
    if n < 5:
        count += n
    elif n > 5:
        count += 10 - n
        N[i + 1] += 1
    elif n == 5:
        if N[i + 1] >= 5:
            N[i + 1] += 1
        count += 5
print(count)
