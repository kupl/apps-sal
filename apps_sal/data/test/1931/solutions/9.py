T = int(input())

for tc in range(T):
    n = int(input())
    count = 0
    while(n >= 2):
        h = (-1 + (1 + 24 * n)**0.5) // 6
        stack_cards = (3 * (h**2) + h) // 2
        count += 1
        n = n - stack_cards

    print(count)
