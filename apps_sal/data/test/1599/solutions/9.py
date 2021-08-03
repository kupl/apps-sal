import sys
f = sys.stdin
#f = open("input.txt", "r")
s = f.readline()
f.readline()
count = [0]
t = ""
q = [map(int, i.split()) for i in f.read().strip().split("\n")]


def solve():
    nonlocal t
    for i in s:
        if i == t:
            count.append(count[-1] + 1)
        else:
            count.append(count[-1])
        t = i
    for i in q:
        l, r = i
        print(count[r] - count[l])


solve()
