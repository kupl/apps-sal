import sys
f = sys.stdin
#f = open("input.txt", "r")
def solve():
    n = int(f.readline())
    b = f.readline()
    count = 0
    if b.count("I") == 1:
        print(1)
        return
    elif b.count("I") > 1:
        print(0)
        return
    else:
        b = b.replace("I", "")
        print(b.count("A"))
solve()
