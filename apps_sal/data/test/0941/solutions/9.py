(lambda b, k, n, N: [[N.__setitem__(0, N[0] * b + i & 1) for i in n], print('odd' if N[0] else 'even')])(*map(int, input().split()), list(map(int, input().split())), [0])
