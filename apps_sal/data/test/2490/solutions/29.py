N = list(map(int, list(input())))
N.reverse()
N = N + [0]
cnt = 0
for i in range(len(N)):
    n = N[i]
    if n < 5:
        cnt += n
    elif n == 5:
        cnt += n
        if N[i + 1] >= 5:
            N[i + 1] += 1
    else:
        cnt += 10 - n
        N[i + 1] += 1
print(cnt)
