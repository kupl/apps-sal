def f_engines():
    import math
    N = int(input())
    # 2πをまたぐようなベクトルの選び方を楽にするため、要素数を2倍
    Engines = sorted([[int(i) for i in input().split()] for j in range(N)],
                     key=lambda x: math.atan2(x[1], x[0])) * 2

    ans = 0
    for head in range(N):
        # 他の人の提出には1重ループのものもあるが、それでいい理屈がわからない
        for tail in range(head, head + N):
            x, y = 0, 0
            for i in range(head, tail + 1):
                dx, dy = Engines[i]
                x += dx
                y += dy
            ans = max(ans, x * x + y * y)
    return math.sqrt(ans)

print(f_engines())
