N = int(input())

answer = 0
for i in range(1, N + 1, 2):
    c = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
    if c == 8:
        answer += 1

print(answer)
