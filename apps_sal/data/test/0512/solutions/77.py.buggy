N = int(input())
state = [(-1, -1) for _ in range(2 * N + 1)]
for i in range(N):
    A, B = map(int, input().split())
    if A != -1 and B == -1:
        if state[A] != (-1, -1):
            print("No")
            return
        state[A] = (0, -1)
    if A == -1 and B != -1:
        if state[B] != (-1, -1):
            print("No")
            return
        state[B] = (1, -1)
    if A != -1 and B != -1:
        if B <= A or state[A] != (-1, -1) or state[B] != (-1, -1):
            print("No")
            return
        state[A] = (0, B - A)
        state[B] = (1, B - A)
dp = [0] * (N + 1)
dp[0] = 1
for i in range(N):
    if dp[i]:
        for k in range(1, N - i + 1):
            flag = True
            for j in range(2 * i + 1, 2 * i + k + 1):
                if state[j][0] == 1:
                    flag = False
                if state[j + k][0] == 0:
                    flag = False
                if state[j][0] == 0 and state[j + k][0] == 1:
                    if not (state[j][1] == k and state[j + k][1] == k):
                        flag = False
                if state[j][0] == 0 and state[j][1] != -1:
                    if state[j][1] != k:
                        flag = False
                if state[j + k][0] == 1 and state[j + k][1] != -1:
                    if state[j][1] != k:
                        flag = False
            if flag:
                dp[i + k] = 1
if dp[N]:
    print("Yes")
else:
    print("No")
