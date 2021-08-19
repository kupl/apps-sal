from collections import deque


def main():
    sas = deque(list(input()))
    sbs = deque(list(input()))
    scs = deque(list(input()))
    deques = {'A': sas, 'B': sbs, 'C': scs}
    player = 'A'
    while True:
        if len(deques[player]) == 0:
            ans = player
            break
        player_temp = deques[player].popleft()
        player = player_temp.upper()
    print(ans)


def __starting_point():
    main()


__starting_point()
