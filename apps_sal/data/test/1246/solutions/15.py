from heapq import heappush , heappop
import sys
inp = sys.stdin.readline

def main():

    heap = []
    ans = []
    n = int(input())

    all = sys.stdin.readlines()
    for ss in all:
        if ss != "removeMin\n":
            a,bb = ss.split(); b = int(bb)

            if a == "insert":
                heappush(heap,b)
            else:
                while heap and heap[0] < b:
                    ans += ['removeMin\n']
                    heappop(heap)
                if not heap or heap[0] != b:
                    ans += ['insert %s\n'%bb]
                    heappush(heap,b)

        else:
            if not heap:
                ans += ['insert 0\n']
            else:
                heappop(heap)

        ans += [ss]

    print(len(ans))
    print("".join(ans))

def __starting_point():
    main()
__starting_point()
