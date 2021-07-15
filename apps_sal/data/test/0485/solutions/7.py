n = int(input())
def check(l):
    a = b = float('inf') # max points
    c = d = 0 # min points
    for x, y in l:
        a = min(a, x)
        b = min(b, y)
        c = max(c, x)
        d = max(d, y)
    borders = [0] * 4
    for x, y in l:
        
        if x in {a, c}:
            if y < b or y > d:
                return False
            if x == a:
                borders[0] += 1
            else:
                borders[1] += 1
        if y in {b, d}:
            if x < a or x > c:
                return False
            if y == b:
                borders[2] += 1
            else:
                borders[3] += 1
        if x not in {a, c} and y not in {b, d}:
            return False
    return all(e >= n for e in borders)


l = [[*map(int, input().split())] for _ in range(4 * n + 1)]

for i in range(len(l)):
    if check(l[:i] + l[i + 1:]):
        print(*l[i])
        return
