from collections import deque


def solve(N):
    dq = deque([(3, [1, 0, 0]), (5, [0, 1, 0]), (7, [0, 0, 1])])
    ans = 0
    while dq:
        (num, check) = dq.popleft()
        if num > N:
            break
        if sum(check) == 3:
            ans += 1
        for i in (3, 5, 7):
            new_num = num * 10 + i
            if new_num > N:
                break
            new_check = check.copy()
            if i == 3:
                new_check[0] = 1
            elif i == 5:
                new_check[1] = 1
            elif i == 7:
                new_check[2] = 1
            dq.append((new_num, new_check))
    print(ans)


def __starting_point():
    N = int(input())
    solve(N)


__starting_point()
