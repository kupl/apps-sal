3

import heapq

def main():
    line1 = input()
    line2 = input()

    n, m = list(map(int, line1.split()))
    l = list(map(int, line2.split()))
    ans = sum(l)
    for i in range(len(l)):
        l[i] *= -1
    heapq.heapify(l)
    for i in range(m):
        price = heapq.heappop(l) * (-1)
        new_price = price // 2
        heapq.heappush(l, new_price * (-1))
        ans -= (price - new_price)
    print(ans)
    return

def __starting_point():
    main()
__starting_point()
