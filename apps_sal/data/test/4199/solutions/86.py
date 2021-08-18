
N, K = list(map(int, input().split()))
my_list = list(map(int, input().split(maxsplit=N)))
answer = 0

for i in range(0, N):
    if my_list[i] >= K:
        answer += 1

print(answer)
