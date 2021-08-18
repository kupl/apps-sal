n, h = list(map(int, input().split()))
bottles = list(map(int, input().split()))


out = 0
for middle in range(n, -1, -1):
    choice = bottles[:middle]
    choice = sorted(choice, reverse=True)
    total_bottles = 0
    current_h = 0
    i = 0
    while i < middle and (current_h + choice[i]) <= h:
        current_h += choice[i]
        i += 2
        total_bottles += 2
    total_bottles = min(total_bottles, middle)
    if total_bottles == middle:
        print(total_bottles)
        break
