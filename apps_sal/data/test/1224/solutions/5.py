import sys
def input(): return sys.stdin.readline().rstrip()
def main():
    n = int(input())
    for a in range(1, 100):
        for b in range(1, 100):
            if 3**a + 5**b == n:
                print(a, b)
                return
    else:
        print(-1)

def __starting_point():
    main()
__starting_point()
