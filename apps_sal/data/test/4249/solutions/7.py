n, m = list(map(int, input().strip().split()))
cups = list(map(int, input().strip().split()))


full_coffe = sum(cups)

if full_coffe < m:
    print("-1")
    return
elif full_coffe == m:
    print(len(cups))
    return

cups.sort(reverse=True)


def check_day(day):
    if day == 0:
        return False
    done = 0
    for idx, c in enumerate(cups):
        done += max(0, c - idx // day)
    return done >= m


lower = 0
upper = n
while upper - lower > 1:
    middle = lower + (upper - lower) // 2
    if check_day(middle):
        upper = middle
    else:
        lower = middle

print(upper)
