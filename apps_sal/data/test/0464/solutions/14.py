n, m = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(input())

seen = set()


def get_first_star():
    r, c = -1, -1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '*':
                seen.add((i, j))
                return i, j
    return r, c


def vertical_points(r, c):
    i = r + 1
    while i < n and arr[i][c] == '*':
        seen.add((i, c))
        i += 1
    return i


def find_horizontal(r, re, c):
    i = r + 1
    found = False
    while i < re - 1:
        if arr[i][c - 1] == '*' and arr[i][c + 1] == '*':
            found = True
            break
        i += 1
    if not found:
        return -1
    j = c - 1
    while j >= 0 and arr[i][j] == '*':
        seen.add((i, j))
        j -= 1
    j = c + 1
    while j < m and arr[i][j] == '*':
        seen.add((i, j))
        j += 1
    return 1


def find_answer():
    r, c = get_first_star()
    if c <= 0 or c >= m - 1:
        return -1

    re = vertical_points(r, c)
    res = find_horizontal(r, re, c)
    if res == -1:
        return -1

    for i in range(n):
        for j in range(m):
            if (i, j) not in seen and arr[i][j] == '*':
                return -1

    return 1


print("YES" if find_answer() == 1 else "NO")
