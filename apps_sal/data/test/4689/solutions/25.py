# coding=utf-8

def __starting_point():
    K, N = map(int, input().split())
    li = list(map(int, input().split()))
    li.append(K + li[0])

    l = 0
    for i in range(N):
        l = max(l, abs(li[i] - li[i + 1]))

    print(K - l)


__starting_point()
