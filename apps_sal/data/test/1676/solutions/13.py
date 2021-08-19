def main():

    def read():
        return list(map(int, input().split()))
    (n, b) = read()
    from collections import deque
    Q = deque()
    ans = [0] * n
    for i in range(n):
        (t, d) = read()
        while len(Q) > 0 and t >= Q[0]:
            Q.popleft()
        if len(Q) == 0:
            cur = t + d
        elif len(Q) < b + 1:
            cur = Q[-1] + d
        else:
            cur = -1
        ans[i] = cur
        if cur != -1:
            Q.append(cur)
    print(' '.join(map(str, ans)))


main()
