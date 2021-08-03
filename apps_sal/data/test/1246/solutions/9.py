from heapq import heappush, heappop


def main():

    heap = []
    ans = []
    n, hsize = int(input()), 0

    for i in range(n):
        ss = input()
        if ss != "removeMin":
            a, bb = ss.split()
            b = int(bb)

            if a == "insert":
                hsize += 1
                heappush(heap, b)
            else:
                while hsize > 0 and heap[0] < b:
                    ans.append('removeMin')
                    hsize -= 1
                    heappop(heap)
                if hsize == 0 or heap[0] != b:
                    ans.append('insert ' + bb)
                    heappush(heap, b)
                    hsize += 1

        else:
            if hsize == 0:
                ans.append('insert 0')
            else:
                heappop(heap)
                hsize -= 1
        ans.append(ss)
    print(len(ans))
    print("\n".join(ans))


def __starting_point():
    main()


__starting_point()
