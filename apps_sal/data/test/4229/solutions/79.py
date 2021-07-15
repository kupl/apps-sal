N = int(input())
N_ = [i for i in range(N + 1)]
N3 = [3 * i for i in range(N // 3 + 1)]
N5 = [5 * i for i in range(N // 5 + 1)]
N15 = [15 * i for i in range(N // 15 + 1)]
print((sum(N_) - sum(N3) - sum(N5) + sum(N15)))
return

