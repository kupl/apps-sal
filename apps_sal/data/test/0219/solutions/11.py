n, m, s, d = [int(i) for i in input().split()]
A = [-1] + sorted([int(i) for i in input().split()]) + [m + 1]
ans_size = 2 * 10**5
ans = [0 for i in range(4 * ans_size)]


def obstacle():
    run = -1
    jump = -1
    top = 0
    for i in range(1, n + 1):
        if s + 2 <= A[i] - A[i - 1]:
            if jump != -1:
                if A[i - 1] + 1 - jump <= d and top > 0 and ans[top - 1][0] == 0 and ans[top - 1][1] >= s:
                    ans[top] = (1, A[i - 1] + 1 - jump)
                    top += 1
                else:
                    print("IMPOSSIBLE")
                    return
            ans[top] = (0, A[i] - A[i - 1] - 2)
            top += 1
            jump = A[i] - 1
    if A[n] + 1 - jump <= d and top > 0 and ans[top - 1][0] == 0 and ans[top - 1][1] >= s:
        ans[top] = (1, A[n] + 1 - jump)
        top += 1
    else:
        print("IMPOSSIBLE")
        return
    if m != A[n] + 1:
        ans[top] = (0, m - A[n] - 1)
        top += 1
    for i in range(top):
        if ans[i][0]:
            print("JUMP", ans[i][1])
        else:
            print("RUN", ans[i][1])


obstacle()
