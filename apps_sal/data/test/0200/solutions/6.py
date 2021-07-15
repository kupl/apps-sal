import math


h1, h2 = list(map(int, input().split()))
day, night = list(map(int, input().split()))

if h2 - h1 <= day * 8:
    print(0)
elif (h2 - h1) - day * 8 + night * 12 - day * 12 <= 0:
    print(1)
elif day - night <= 0:
    print(-1)
else:

    # (h2 - h1) <= k * (day - night) * 12 + day * 12 + day * 8 - night * 12

    print((
        int(math.ceil(
            ((h2 - h1) - day * 20 + night * 12) / ((day - night) * 12)
        )) + 1
    ))

