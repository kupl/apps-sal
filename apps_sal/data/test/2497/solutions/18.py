n = int(input())
xyd = [input().split() for _ in range(n)]


x_max_RL_ = [-2e8] * 3
x_min_RL_ = [2e8] * 3
y_max_UD_ = [-2e8] * 3
y_min_UD_ = [2e8] * 3

for x, y, d in xyd:
    x = int(x)
    y = int(y)

    if d == "R":
        ho, ve = 2, 1
    elif d == "L":
        ho, ve = 0, 1
    elif d == "U":
        ho, ve = 1, 2
    else:
        ho, ve = 1, 0
    x_max_RL_[ho] = max(x_max_RL_[ho], x)
    x_min_RL_[ho] = min(x_min_RL_[ho], x)
    y_max_UD_[ve] = max(y_max_UD_[ve], y)
    y_min_UD_[ve] = min(y_min_UD_[ve], y)

kouho_time = set([0])

for _max_min in [x_max_RL_, x_min_RL_, y_max_UD_, y_min_UD_]:
    for i in range(0, 3):
        if abs(_max_min[i]) <= 1e8:
            for j in range(i + 1, 3):
                if abs(_max_min[j]) <= 1e8:
                    cross = (_max_min[i] - _max_min[j]) / (j - i)
                    if cross > 0:
                        kouho_time.add(cross)


ans = 4e16
for t in kouho_time:
    x_max = max(
        x_max_RL_[i] + t * (i - 1) for i in range(3) if abs(x_max_RL_[i]) <= 1e8
    )
    x_min = min(
        x_min_RL_[i] + t * (i - 1) for i in range(3) if abs(x_min_RL_[i]) <= 1e8
    )
    y_max = max(
        y_max_UD_[i] + t * (i - 1) for i in range(3) if abs(y_max_UD_[i]) <= 1e8
    )
    y_min = min(
        y_min_UD_[i] + t * (i - 1) for i in range(3) if abs(y_min_UD_[i]) <= 1e8
    )

    ans = min(ans, (x_max - x_min) * (y_max - y_min))

print(ans)
