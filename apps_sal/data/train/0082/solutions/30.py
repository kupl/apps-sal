

def main():
    n = int(input())
    p = list(map(int,input().split()))
    p = list(reversed(p))
    for i in p:
        print(i, end=" ")
    print()


def __starting_point():
    t = int(input())
    for i in range(t):
        main()
"""
60, 61
"""
"""
"""

__starting_point()
