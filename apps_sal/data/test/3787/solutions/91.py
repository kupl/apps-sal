import sys
from bisect import bisect


def Longest_Increasing_Subsequence(N, lst):
    # 配列の長さがN、配列がlstで与えられる最長増加部分列を返す
    # O(NlogN)

    MM = max(lst) + 1
    data = [MM] * (N + 1)
    # MMは配列の最大値とする
    # infだと計算量が結構大きくなるため

    data[0] = 0
    for i in range(N):
        b = bisect(data, lst[i])
        data[b] = lst[i]

    ANS = 1
    for i in range(1, N + 1):
        if data[i] != MM:
            ANS = i

    return ANS


def Longest_Decreasing_Subsequence(N, lst):
    # 配列の長さがN、配列がlstで与えられる最長減少部分列を返す
    # O(NlogN)

    MM = max(lst) + 1
    data = [MM] * (N + 1)
    # MMは配列の最大値とする

    # 配列を逆にして、最長増加部分列を求めればいよい
    lst = lst[::-1]

    data[0] = 0
    for i in range(N):
        b = bisect(data, lst[i])
        data[b] = lst[i]

    ANS = 1
    for i in range(1, N + 1):
        if data[i] != MM:
            ANS = i

    return ANS


N, A, B = map(int, input().split())
AAA, BBB = A, B

if A > N or B > N:
    print(-1)
    return
if B > N - A + 1:
    print(-1)
    return

ans = []
L = 1
R = N
flag = [0] * (N + 1)
flag[0] = 1

if A < B:
    B -= 1
    while A > 0 and B > 0 and len(ans) < N:
        for i in range(max(1, R - A + 1), R + 1):
            if flag[i] == 0:
                flag[i] = 1
                ans.append(i)
        R -= A
        A -= 1
        for i in range(min(N, L + B - 1), L - 1, -1):
            if flag[i] == 0:
                flag[i] = 1
                ans.append(i)
        L += B
        B -= 1

    for i in range(min(N, L + B - 1), L - 1, -1):
        if flag[i] == 0:
            flag[i] = 1
            ans.append(i)

elif A == B:
    B -= 1
    while A > 0 and B > 0 and len(ans) < N:
        for i in range(max(1, R - A + 1), R + 1):
            if flag[i] == 0:
                flag[i] = 1
                ans.append(i)
        R -= A
        A -= 1
        for i in range(min(N, L + B - 1), L - 1, -1):
            if flag[i] == 0:
                flag[i] = 1
                ans.append(i)
        L += B
        B -= 1

    for i in range(max(1, R - A + 1), R + 1):
        if flag[i] == 0:
            flag[i] = 1
            ans.append(i)

else:
    A -= 1
    while A > 0 and B > 0 and len(ans) < N:
        for i in range(min(N, L + B - 1), L - 1, -1):
            if flag[i] == 0:
                flag[i] = 1
                ans.append(i)
        L += B
        B -= 1
        for i in range(max(1, R - A + 1), R + 1):
            if flag[i] == 0:
                flag[i] = 1
                ans.append(i)
        R -= A
        A -= 1

    for i in range(max(1, R - A + 1), R + 1):
        if flag[i] == 0:
            flag[i] = 1
            ans.append(i)

if len(ans) >= N:
    ans = ans[:N]
    if Longest_Increasing_Subsequence(N, ans) == AAA and Longest_Decreasing_Subsequence(N, ans) == BBB:
        print(*ans)
    else:
        print(-1)
else:
    print(-1)
