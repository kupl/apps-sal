from heapq import heappop, heappush


def main():
    (n, c) = list(map(int, input().split()))
    program = [[] for _ in range(c)]
    for _ in range(n):
        (s, t, cc) = list(map(int, input().split()))
        cc -= 1
        s *= 2
        t *= 2
        program[cc].append([s - 1, t])
    all_p = []
    for i in range(c):
        if len(program[i]) == 0:
            continue
        now = program[i]
        now.sort(key=lambda x: x[1])
        (last_begin, last_end) = now[0]
        for (begin, end) in now[1:]:
            if begin + 1 == last_end:
                last_end = end
            else:
                all_p.append([last_begin, last_end, i])
                last_begin = begin
                last_end = end
        all_p.append([last_begin, last_end, i])
    all_p.sort()
    q = [(-1, -1)]
    for (begin, end, now_channel) in all_p:
        (last_end, last_channel) = q[0]
        if last_end < begin or now_channel == last_channel:
            heappop(q)
        heappush(q, (end, now_channel))
    print(len(q))


def __starting_point():
    main()


__starting_point()
