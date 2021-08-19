def main():
    N = int(input())
    A = [int(a) - 1 for a in input().split(' ')]
    int_cnt = [0] * N
    for a in A:
        int_cnt[a] += 1
    S = sum([combination_2(c) for c in int_cnt])
    for i in range(N):
        x = int_cnt[A[i]]
        print(S - combination_2(x) + combination_2(x - 1))


def combination_2(n):
    return int(n * (n - 1) / 2)


main()
