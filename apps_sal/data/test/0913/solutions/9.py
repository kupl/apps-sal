import string


def main():
    n = int(input())
    r = list(map(int, input().split()))
    b = list(map(int, input().split()))
    more = 0
    less = 0
    for i in range(n):
        if r[i] > b[i]:
            more += 1
        elif r[i] < b[i]:
            less += 1
    if more == 0:
        print(-1)
        return
    a = less/more + 1
    print(int(a))

def __starting_point():
    t = 1
    for i in range(t):
        main()

__starting_point()
