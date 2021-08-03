N, K = map(int, input().split())
h = list(map(int, input().split()))

answer = 0

for i in h:
    if i >= K:
        answer += 1

print(answer)
