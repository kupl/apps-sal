N = list(map(int, list(input())))[::-1]
L = len(N)

answer = 0
for i, n in enumerate(N):
    if n < 5:
        answer += n
    elif n > 5:
        answer += 10 - n
        if i < L - 1:
            N[i + 1] += 1
        else:
            answer += 1
    else:
        answer += 5
        if i < L - 1:
            if N[i + 1] >= 5:
                N[i + 1] += 1

print(answer)
