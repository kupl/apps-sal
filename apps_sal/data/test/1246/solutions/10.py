from heapq import heappush, heappop


def main():

    heap = []
    ans = []
    n, hsize = int(input()), 0

    for i in range(n):
        ss = input()
        if ss != "removeMin":
            a, bb = ss.split(); b = int(bb)

            if a == "insert":
                hsize += 1
                heappush(heap, b)
            else:
                while hsize > 0 and heap[0] < b:
                    ans += ['removeMin']
                    hsize -= 1
                    heappop(heap)
                if hsize == 0 or heap[0] != b:
                    ans += ['insert ' + bb]
                    heappush(heap, b)
                    hsize += 1

        else:
            if hsize == 0:
                ans += ['insert 0']
            else:
                heappop(heap)
                hsize -= 1
        ans += [ss]
    print(len(ans))
    print("\n".join(ans))


main()
