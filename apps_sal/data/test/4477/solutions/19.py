t = int(input())
for _ in range(t):
    n = int(input())
    counting = 0
    is_done = False
    for i in range(1, 10):
        for c in range(1, 5):
            curr_int = int(str(i) * c)
            counting += c
            if curr_int == n:
                print(counting)
                is_done = True
                break
        if is_done:
            break
