import math

def read_data():
    n = int(input().strip())
    return n

def compare(s):
    mpos = 0
    spos = 0
    count = 0
    while spos < len(s):
        npos = m.find(s[spos],mpos)
        if npos == -1:
            return -1
        count += npos - mpos
        mpos = npos + 1
        spos += 1
    count += len(m) - mpos
    return count

def solve():
    start = int(math.sqrt(n))
    for i in range(start,0,-1):
        c = compare(str(i*i))
        if c > -1:
            return c
    return -1

n = read_data()
m = str(n)
print(solve())
