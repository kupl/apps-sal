import math
N = int(input())
engines = tuple((complex(*map(int, input().split())) for _ in range(N)))
engines = sorted(list((engine, math.atan2(engine.imag, engine.real))for engine in engines if engine != 0), key=lambda x: x[1])
N = len(engines)
if N == 0:
    print(0)
else:
    total = sum(engine[0] for engine in engines)
    head_index = max(i if engines[i][0].imag < 0 else -1 for i in range(N))
    tail_index = 0
    tmp = sum(engines[i][0] for i in range(tail_index, head_index + 1))
    maximum = max(abs(tmp), abs(total - tmp))

    while True:
        if head_index < N - 1:
            if (engines[head_index + 1][0] / engines[tail_index][0]).imag >= 0:
                head_index += 1
            else:
                tail_index += 1
        else:
            if (engines[0][0] / engines[tail_index][0]).imag < 0:
                tail_index += 1
            else:
                break
        tmp = sum(engines[i][0] for i in range(tail_index, head_index + 1))
        maximum = max(maximum, abs(tmp), abs(total - tmp))

    print(maximum)
