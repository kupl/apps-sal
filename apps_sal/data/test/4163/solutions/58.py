import numpy as np

N = int(input())

dice = [input() for i in range(N)]
DICE = np.array([[int(i.split()[0]), int(i.split()[1])] for i in dice])


a1 = np.where(DICE[:-2, 0] == DICE[:-2, 1], 1, 0)
a2 = np.where(DICE[1:-1, 0] == DICE[1:-1, 1], 1, 0)
a3 = np.where(DICE[2:, 0] == DICE[2:, 1], 1, 0)

if sum(a1 * a2 * a3) > 0:
    print('Yes')
else:
    print('No')
