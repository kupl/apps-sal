(N, M) = list(map(int, input().split()))
height_list = list(map(int, input().split()))
road_list_1 = [list(map(int, input().split())) for i in range(M)]
road_list = [[road_list_1[j][i] - 1 for i in range(2)] for j in range(M)]
observation_deck = list(range(N))
for i in range(M):
    if height_list[road_list[i][0]] >= height_list[road_list[i][1]]:
        observation_deck[road_list[i][1]] = -1
    if height_list[road_list[i][0]] <= height_list[road_list[i][1]]:
        observation_deck[road_list[i][0]] = -1
answer = 0
for i in range(N):
    if observation_deck[i] != -1:
        answer += 1
print(answer)
