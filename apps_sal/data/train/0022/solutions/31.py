import sys, os

if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')

f = lambda:list(map(int, input().split()))


midigit = lambda x: str(x)
def solve():
    t = f()[0]
    for _ in range(t):
        a, k = f()
        if k == 1:
            print(a)
            continue
        for i in range(k-1):
            an = a + int(min(str(a))) * int(max(str(a)))
            if a == an:
                break
            a = an
        print(a)

solve()

