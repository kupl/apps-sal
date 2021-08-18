def main():
    N, M = list(map(int, input().split()))
    if abs(N - M) > 1:
        return 0
    N_mlt = 1
    M_mlt = 1
    for i in range(1, N + 1, 1):
        N_mlt *= i
        N_mlt = N_mlt % 1000000007
    for i in range(1, M + 1, 1):
        M_mlt *= i
        M_mlt = M_mlt % 1000000007
    ans = (N_mlt * M_mlt) % 1000000007
    if abs(N - M) == 0:
        ans = (ans * 2) % 1000000007
        return ans
    else:
        return ans


print((main()))
