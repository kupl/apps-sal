S_s = [input() for _ in range(3)]
turn = 0
pos = [0, 0, 0]
dic = {'a': 0, 'b': 1, 'c': 2}
while 1:
    try:
        n_turn = dic[S_s[turn][pos[turn]]]
        pos[turn] += 1
        turn = n_turn
    except IndexError:
        break
print('ABC'[turn])
