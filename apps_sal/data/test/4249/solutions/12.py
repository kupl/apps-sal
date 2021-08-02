def check_possibility(days, m, coffee):
    sum_coffee = 0
    for i, cup in enumerate(coffee):
        tax = i // days
        if sum_coffee >= m or tax >= cup:
            break
        sum_coffee += cup - tax
    return sum_coffee >= m


n, m = list(map(int, input().split()))
coffee = sorted(map(int, input().split()), reverse=True)

bad = 0
good = len(coffee)

while good - bad > 1:
    days = (bad + good) // 2
    if check_possibility(days, m, coffee):
        good = days
    else:
        bad = days

possible = check_possibility(good, m, coffee)
print(good if possible else -1)
