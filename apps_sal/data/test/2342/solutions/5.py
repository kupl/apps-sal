import sys
strings = iter(sys.stdin.read().split())
ints = (int(x) for x in strings)
sys.setrecursionlimit(3000)

def block(m,R,C,esc,r,c):
    if esc[r][c]==0:
        return 1
    q = [(r,c)]
    h = set([(r,c)])
    while q:
        r,c = q.pop()
        if m[r][c]=='.':
            m[r][c]='#'
        if m[r][c]!='#' and r==R-1 and c==C-1:
            return 0
        if m[r][c]!='#':
            for r,c in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0<=r<R and 0<=c<C and (r,c) not in h:
                    q.append((r,c))
                    h.add((r,c))
    for r,c in h:
        esc[r][c] = 0
    return 1

def reachability(m,R,C):
    esc = [[0 for c in range(C)] for r in range(R)]
    q = [(R-1,C-1)]
    while q:
        r,c = q.pop()
        esc[r][c] = 1
        if m[r][c]!='#':
            for r,c in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0<=r<R and 0<=c<C and esc[r][c]==0:
                    q.append((r,c))
    return esc

def main():
    ntc = next(ints)
    for tc in range(1,ntc+1):
        R,C = (next(ints) for i in range(2))
        m = [list(next(strings)) for r in range(R)]
        B = [(r,c) for r in range(R) for c in range(C) if m[r][c]=='B']
        G = [(r,c) for r in range(R) for c in range(C) if m[r][c]=='G']
        esc = reachability(m,R,C)
        ans = all(esc[r][c] for r,c in G)
        if ans:
            ans = all(block(m,R,C,esc,r,c) for r,c in B)
        if ans:
            esc = reachability(m,R,C)
            ans = all(esc[r][c] for r,c in G)
        print('Yes' if ans else 'No')
    return

main()

