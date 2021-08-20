from collections import Counter


def __starting_point():
    N = int(input())
    C = Counter()
    march = ['M', 'A', 'R', 'C', 'H']
    for _ in range(N):
        s = input()
        if s[0] in march:
            C[s[0]] += 1
    ans = 0
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                ans += C[march[i]] * C[march[j]] * C[march[k]]
    print(ans)


__starting_point()
