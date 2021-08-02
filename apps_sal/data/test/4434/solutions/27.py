T = int(input())

for t in range(T):
    N = int(input())

    answer = 0
    i = 0
    moves = 0
    nb = 0
    while i < N // 2:
        i += 1
        nb += 8
        answer += nb * i
    print(answer)
