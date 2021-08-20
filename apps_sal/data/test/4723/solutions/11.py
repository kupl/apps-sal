import sys
stdin = sys.stdin


def ns():
    return stdin.readline().rstrip()


def ni():
    return int(stdin.readline().rstrip())


def nm():
    return list(map(int, stdin.readline().split()))


def nl():
    return list(map(int, stdin.readline().split()))


def can_replace(S, T):
    cnt = 0
    for (s, t) in zip(S, T):
        if s == t or s == '?':
            cnt += 1
    if cnt == len(S):
        return True
    else:
        return False


def main():
    S = list(ns()[::-1])
    T = list(ns()[::-1])
    for i in range(len(S) - len(T) + 1):
        if can_replace(S[i:i + len(T)], T):
            S[i:i + len(T)] = T
            S = ''.join(S)
            print(S.replace('?', 'a')[::-1])
            return
    print('UNRESTORABLE')


def __starting_point():
    main()


__starting_point()
