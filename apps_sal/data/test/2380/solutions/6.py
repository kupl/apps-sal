import heapq
push, pop = heapq.heappush, heapq.heappop

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))


def modify():
    heapq.heapify(a)

    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)

    for b, c in bc:
        for _ in range(b):
            p = pop(a)
            if p < c:
                push(a, c)
            else:
                # キューに戻す
                push(a, p)
                return


modify()
print(sum(a))
