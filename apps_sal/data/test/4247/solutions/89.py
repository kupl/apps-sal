n = int(input())
p = list(map(int, input().split()))
answer = 0
for i in range(n - 2):
    if p[i] < p[i + 1] < p[i + 2] or p[i + 2] < p[i + 1] < p[i]:
        answer += 1
print(answer)
