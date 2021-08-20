N = int(input())
answer = 1000000000000
for i in range(1, int(N ** 0.5) + 2):
    if N % i == 0:
        j = N // i
        if i + j - 2 < answer:
            answer = i + j - 2
print(answer)
