def check():
    N = int(input())
    plus, minus = [], []
    for i in range(N):
        S = input()
        now = 0
        mini = 0
        for s in S:
            if s == '(':
                now += 1
            else:
                now -= 1
                mini = min(mini, now)
        if now >= 0:
            plus.append([mini, now])
        else:
            minus.append([now - mini, now])
    plus.sort(reverse=True)
    minus.sort(reverse=True)
    now = 0
    for a, b in plus:
        if now + a < 0:
            return 'No'
        now += b
    for a, b in minus:
        if now + b - a < 0:
            return 'No'
        now += b
    if now > 0:
        return 'No'
    return 'Yes'


print(check())
