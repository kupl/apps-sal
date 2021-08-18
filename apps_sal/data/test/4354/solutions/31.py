N, M = map(int, input().split())

A_B = [list(map(int, input().split())) for _ in range(N)]
C_D = [list(map(int, input().split())) for _ in range(M)]


for a, b in A_B:
    temp_distance = 10**10
    temp_checkpoint = -1
    checkpoint_count = 1
    for c, d in C_D:
        manhattan_distance = abs(a - c) + abs(b - d)
        if temp_distance > manhattan_distance:
            temp_distance = manhattan_distance
            temp_checkpoint = checkpoint_count
        checkpoint_count += 1
    print(temp_checkpoint)
