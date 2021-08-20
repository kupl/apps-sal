n = int(input())


def maruta(m):
    if n + 1 >= m * (m + 1) // 2:
        return True
    else:
        False


left = 1
right = n + 1
while left + 1 < right:
    t = (left + right) // 2
    if maruta(t):
        left = t
    else:
        right = t
print(n + 1 - left)
