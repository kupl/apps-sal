import numpy as np

N = int(input())

S = input()

base_ascii = 65

als = [chr(a) for a in range(65, 90 + 1)]

ascii_S = np.array(list(map(ord, S))) - base_ascii

print(''.join([als[np.mod(s + N, len(als))] for s in ascii_S]))
