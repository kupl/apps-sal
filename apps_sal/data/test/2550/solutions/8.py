

"""
NTC here
"""
import sys
inp = sys.stdin.readline
def input(): return inp().strip()
# flush= sys.stdout.flush
# import threading
# sys.setrecursionlimit(10**6)
# threading.stack_size(2**26)


def iin(): return int(input())


def lin(): return list(map(int, input().split()))


def main():
    T = iin()
    while T:
        T-=1
        n, m = lin()
        a = lin()
        ans = sum(a)
        print(min(ans, m))


main()

# threading.Thread(target=main).start()


"""
1
5
1 3
1 4
1 6
2 6
0 5
"""
