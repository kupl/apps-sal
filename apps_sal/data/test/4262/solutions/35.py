import itertools
N = int(input())
N_list = [i for i in range(1, N + 1)]
P = list(itertools.permutations(N_list))
P.sort()
Q = tuple(map(int, input().split()))
O = tuple(map(int, input().split()))
Q_number = P.index(Q) + 1
O_number = P.index(O) + 1
print(abs(Q_number - O_number))
