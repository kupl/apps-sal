n = int(input())
p = list(map(int, input().split()))

answer = 0
for i in range(n - 2):
    if p[i] < p[i + 1] < p[i + 2]:
        answer += 1
    if p[i] > p[i + 1] > p[i + 2]:
        answer += 1

print(answer)
