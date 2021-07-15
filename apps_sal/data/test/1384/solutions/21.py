n = int(input())

l = list(map(int, input().split()))

max_games = [1 for i in range(n)]

if n > 1:
    if l[1] == 0:
        if l[0] == 1:
            max_games[1] = 1
        else:
            max_games[1] = 2
    else:
        max_games[1] = 2

t_max = max(max_games)

if n > 2:
    for i in range(2, n):
        if l[i] == 0:
            j = i - 1
            while (j >= 0):
                if l[j] == 0:
                    max_games[i] = max_games[j] + 1
                    t_max = max([t_max, max_games[i]])
                    break
                j -= 1
        else:
            max_games[i] = t_max + 1
            t_max += 1



print(t_max)

