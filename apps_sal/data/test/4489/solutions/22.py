N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]


def ans091(N: int, s: list, M: int, t: list):
    test_count = 0
    own = list(set(s))
    for i in range(len(own)):
        if test_count <= s.count(own[i]) - t.count(own[i]):
            test_count = s.count(own[i]) - t.count(own[i])
    if test_count > 0:
        return test_count
    else:
        return 0


print(ans091(N, s, M, t))
