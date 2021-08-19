from collections import deque


def solve():
    N = int(input())
    Ss = list(map(int, input().split()))
    Ss.sort(reverse=True)
    Qs = [deque() for _ in range(N + 1)]
    Qs[0].append(10 ** 10)
    for S in Ss:
        for day in range(N + 1):
            if not Qs[day]:
                continue
            if Qs[day][0] > S:
                Qs[day].popleft()
                for d in range(day + 1, N + 1):
                    Qs[d].append(S)
                break
        else:
            return False
    return True


if solve():
    print('Yes')
else:
    print('No')
