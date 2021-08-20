(N, M) = list(map(int, input().split()))
p_allac = (1 / 2) ** M
ref = 2 ** M
T = 100 * (N - M) + 1900 * M
print(T * ref)
