import heapq


def run():
    n, k, d = list(map(int, input().split()))
    a = sorted(map(int, input().split()))

    max_size = [None] * n  # how many pencils can be in box starting with this one
    start = 0
    end = 0
    while start < n:
        while end < n - 1 and a[end + 1] - a[start] <= d:
            end += 1
        max_size[start] = end - start + 1
        start += 1

    possilbe_starts = []
    # heap with starts and stops of intervals where new box can start
    # - all pencils before that are successfully boxed
    heapq.heappush(possilbe_starts, (0, "start"))
    heapq.heappush(possilbe_starts, (1, "stop"))

    number_of_opened = 0  # number of opened intervals

    for pencil in range(n):
        while possilbe_starts and possilbe_starts[0][0] <= pencil:
            top = heapq.heappop(possilbe_starts)
            number_of_opened += (1 if top[1] == "start" else -1)
        if number_of_opened <= 0:
            continue
        if max_size[pencil] < k:
            continue
        if pencil + max_size[pencil] + 1 > n:
            print("YES")
            break
        heapq.heappush(possilbe_starts, (pencil + k, "start"))
        heapq.heappush(possilbe_starts, (pencil + max_size[pencil] + 1, "stop"))
    else:
        print("NO")


run()
