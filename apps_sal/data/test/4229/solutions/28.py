N = int(input())
answer = 0

for i in range(1, N + 1):
    if i % 3 != 0 and i % 5 != 0:
        answer += i

print(answer)
