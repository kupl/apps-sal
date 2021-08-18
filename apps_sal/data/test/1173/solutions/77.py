def is_not_empty(A):
    for x in A:
        if x:
            return True
    return False


def main():
    import sys
    input = sys.stdin.readline
    from collections import deque

    N = int(input())
    A = [deque() for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in input().split():
            A[i].append(int(j))

    today = set()
    for i in range(1, N + 1):
        if i in today:
            continue
        enemy = A[i].popleft()
        ME = A[enemy].popleft()
        if ME == i and not(enemy in today):
            today.add(ME)
            today.add(enemy)
        else:
            A[i].appendleft(enemy)
            A[enemy].appendleft(ME)
    if not today:
        print(-1)
        return

    yesterday = today
    answer = 1
    while is_not_empty(A):
        today = set()
        for i in yesterday:
            if not A[i]:
                continue
            if i in today:
                continue
            enemy = A[i].popleft()
            ME = A[enemy].popleft()
            if ME == i and not(enemy in today):
                today.add(ME)
                today.add(enemy)
            else:
                A[i].appendleft(enemy)
                A[enemy].appendleft(ME)
        if not today:
            print(-1)
            return
        answer += 1
        yesterday = today

    print(answer)


def __starting_point():
    main()


__starting_point()
