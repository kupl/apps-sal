import numpy as np

N = int(input())

S = input()

ascii_S = np.array(list(map(ord, S))) - 65

shift_ascii_S = list(map(lambda x: 65 + np.mod(x + N, 26), ascii_S))

shift_S = ''.join(list(map(chr, shift_ascii_S)))

print(shift_S)
