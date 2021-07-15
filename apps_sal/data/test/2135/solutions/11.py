
def solve(h, w, board, queries):

    def get_horiz(h, w, board):
        horiz = [[None] * w for _ in range(h)]
        for i in range(w):
            for j in range(h):
                if i == 0:
                    horiz[j][i] = 0
                    continue
                current = 1 if (board[j][i] == '.' and board[j][i-1] == '.') else 0
                if j == 0:
                    horiz[j][i] = horiz[j][i-1] + current
                else:
                    current = 1 if (board[j][i] == '.' and board[j][i-1] == '.') else 0
                    horiz[j][i] = horiz[j][i-1] + horiz[j-1][i] - horiz[j-1][i-1] + current
        return horiz

    trans = [[None] * h for _ in range(w)]
    for i in range(w):
        for j in range(h):
            trans[i][j] = board[j][i]

    horiz = get_horiz(h, w, board)
    vert = get_horiz(w, h, trans)

    def query(r1, c1, r2, c2):
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1
        acum = 0
        for rr1, rr2, cc1, cc2, horizvert in [(r1, r2, c1, c2, horiz), (c1, c2, r1, r2, vert)]:
            base = horizvert[rr2][cc2]
            if rr1 > 0:
                base -= horizvert[rr1 - 1][cc2]
                base += horizvert[rr1 - 1][cc1]
            base -= horizvert[rr2][cc1]
            acum += base
        return acum

    #print(get_horiz(h, w, board))
    #print(query(1,2,4,5))
    res = []
    for q in queries:
        res.append(query(*q))
    return res

h, w = tuple(map(int, input().split()))
board = []
for _ in range(h):
    board.append(input())
qnum = int(input())
queries = []
for _ in range(qnum):
    queries.append(tuple(map(int, input().split())))
res = solve(h, w, board, queries)
for r in res:
    print(r)

