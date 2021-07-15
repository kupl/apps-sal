R = lambda: map(int, input().split())

def func():
    n, m = R()
    cnt = [0]*m
    ss = []

    for i in range(n):
        s = input()
        ss.append(s)
        for j, ch in enumerate(s):
            if ch == '1': cnt[j] += 1

    for i in range(n):
        s = ss[i]
        for j, ch in enumerate(s):
            if ch == '1' and cnt[j] <= 1: break
        else:
            return 1

    return 0


print('YES' if func() else 'NO')
