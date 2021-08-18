import sys
def input(): return sys.stdin.readline().strip()


def f(A, r, c, l):
    q, w, e = A[r][c][0], A[r][c - l][0], A[r][c - 2 * l][0]
    x, y, z = A[r][c][1], A[r][c - l][1], A[r][c - 2 * l][1]

    if x != y and y != z and e >= l and w == q == l:
        return (l, z, y, x)
    else:
        return 0


r, c = list(map(int, input().split()))
s = ""
for i in range(r):
    s += input()

arr = []
narr = [[0] * r for i in range(c)]
for i in range(c):
    arr.append(s[i:r * c:c])

r, c = c, r

length_str = [[0] * c for i in range(r)]
for i in range(r):
    for j in range(c):
        if j == 0:
            length_str[i][j] = (1, arr[i][j])
        elif arr[i][j - 1] == arr[i][j]:
            length_str[i][j] = (length_str[i][j - 1][0] + 1, arr[i][j])
        else:
            length_str[i][j] = (1, arr[i][j])

for i in range(r):
    for j in range(c):
        l, _ = length_str[i][j]
        if j - l * 3 + 1 < 0:
            continue
        else:
            narr[i][j] = f(length_str, i, j, l)


dp = [[0] * c for i in range(r)]


for j in range(c):
    cnt = 1
    for i in range(r):
        if narr[i][j] == 0:
            cnt = 1
            continue
        else:
            if i == 0:
                dp[i][j] = 1

            elif narr[i][j] == narr[i - 1][j]:
                cnt += 1
                dp[i][j] = cnt
                dp[i - 1][j] = 0

            else:
                cnt = 1
                dp[i][j] = 1

ans = 0
for i in dp:
    for j in i:
        ans += ((j) * (j + 1)) // 2

print(ans)
