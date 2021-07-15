import sys
f = sys.stdin
#f = open("input.txt", "r")
l = [int(i) for i in f.readline().strip().split()]
n, s, t = l[0], l[1], l[2]
p = [int(i) for i in f.readline().strip().split()]
def solve():
    count = 0
    b = s
    if (s == p.index(s)+1 or t == p.index(t)+1) and t != s:
        count = -1
    else:
        while b != t:
            b = p[b-1]
            count += 1
            if count >= n:
                count = -1
                break
    print(count)
solve()
