# coding: utf-8

def main():
    N, M = list(map(int, input().split()))
    imos = [0] * (N + 2)
    ans = 0

    for _ in range(M):
        l, r = list(map(int, input().split()))
        imos[l] += 1
        imos[r + 1] -= 1

    for i in range(1, N + 2):
        imos[i] += imos[i - 1]
        if imos[i] == M and i != N + 1:
            ans += 1
    
    print(ans)

def __starting_point():
    main()

__starting_point()
