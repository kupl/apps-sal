t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    hand_size = n // k
    my_hand = min(hand_size, m)
    m -= my_hand

    if m % (k - 1) == 0:
        next_hand = m // (k - 1)
    else:
        next_hand = m // (k - 1) + 1

    print(my_hand - next_hand)
