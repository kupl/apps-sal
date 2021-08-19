def solve():
    answer = [0] * m
    for i in range(1, n):
        for j in range(m):
            if j - i >= 0:
                if park[i][j - i] == 'R':
                    answer[j] += 1
            if j + i < m:
                if park[i][j + i] == 'L':
                    answer[j] += 1
            if 2 * i < n:
                if park[2 * i][j] == 'U':
                    answer[j] += 1
    return answer


(n, m, k) = tuple(map(int, input().split()))
park = [input() for i in range(n)]
print(' '.join(map(str, solve())))
