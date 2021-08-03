r, g, b = list(map(int, input().split()))


def work(mix):
    if mix > min(r, g, b):
        return 0
    else:
        return ((r - mix) // 3 +
                (g-mix) // 3 +
                (b-mix) // 3 +
                mix)


print(max(work(0), work(1), work(2)))
