n = int(input())
AB = tuple(tuple(map(int, input().split())) for _ in range(n))
C = [(-1, -1)] * (2 * n + 1)
for i, (a, b) in enumerate(AB):
    if a == -1 and b == -1:
        continue
    if a == -1:
        if C[b][0] != -1:
            print("No")
            return
        C[b] = (1, i)
        continue
    if b == -1:
        if C[a][0] != -1:
            print("No")
            return
        C[a] = (0, i)
        continue
    if a >= b:
        print("No")
        return
    if C[a][0] != -1 or C[b][0] != -1:
        print("No")
        return
    C[a] = (0, i)
    C[b] = (1, i)


def f(l, r):
    m = (r - l + 1) // 2
    for i in range(l, l + m):
        left_direct, left_idx = C[i]
        right_direct, right_idx = C[i + m]
        if left_direct == 1 or right_direct == 0:
            return False
        if left_direct != -1 and right_direct != -1:
            if left_idx != right_idx:
                return False
            continue
        if left_direct != -1:
            left_b = AB[left_idx][1]
            if left_b != -1 and i + m != left_b:
                return False
        if right_direct != -1:
            right_a = AB[right_idx][0]
            if right_a != -1 and i != right_a:
                return False
    return True


dp = [False] * (n + 1)
dp[0] = True
for i in range(n):
    if not dp[i]:
        continue
    for j in range(i + 1, n + 1):
        if f(2 * i + 1, 2 * j):
            dp[j] = True
if dp[n]:
    print("Yes")
else:
    print("No")
