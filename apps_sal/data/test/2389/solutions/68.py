N, A, B, C = map(int, input().split())
dt = {'AB': (0, 1), 'AC': (0, 2), 'BC': (1, 2)}
Q = [dt[input()] for _ in range(N)]


class Game:
    def __init__(self, ABC):
        self.ABC = ABC
        self.ds = {0: 'A', 1: 'B', 2: 'C'}
        self.ans = []

    def add_q0(self, q0, q1):
        self.ans.append(self.ds[q0])
        self.ABC[q0] += 1
        self.ABC[q1] -= 1

    def add_q1(self, q0, q1):
        self.ans.append(self.ds[q1])
        self.ABC[q0] -= 1
        self.ABC[q1] += 1


def solve1(ABC):
    G = Game(ABC)
    for q0, q1 in Q:
        if G.ABC[q0] == G.ABC[q1] == 0:
            print('No')
            return
        elif G.ABC[q0] == 0:
            G.add_q0(q0, q1)
        else:
            G.add_q1(q0, q1)
    print('Yes')
    print(*G.ans, sep='\n')


def solve2(ABC):
    G = Game(ABC)
    for i, (q0, q1) in enumerate(Q):
        if G.ABC[q0] == G.ABC[q1] == 0:
            print('No')
            return
        elif G.ABC[q0] == 0:
            G.add_q0(q0, q1)
        elif G.ABC[q1] == 0:
            G.add_q1(q0, q1)
        elif G.ABC[q0] == G.ABC[q1] == 1 and i < N - 1:
            if q0 in Q[i + 1]:
                G.add_q0(q0, q1)
            else:
                G.add_q1(q0, q1)
        else:
            if G.ABC[q0] <= G.ABC[q1]:
                G.add_q0(q0, q1)
            else:
                G.add_q1(q0, q1)
    print('Yes')
    print(*G.ans, sep='\n')


def solve3(ABC):
    G = Game(ABC)
    for q0, q1 in Q:
        if G.ABC[q0] == G.ABC[q1] == 0:
            print('No')
            return
        elif G.ABC[q0] == 0:
            G.add_q0(q0, q1)
        elif G.ABC[q1] == 0:
            G.add_q1(q0, q1)
        else:
            if G.ABC[q0] <= G.ABC[q1]:
                G.add_q0(q0, q1)
            else:
                G.add_q1(q0, q1)
    print('Yes')
    print(*G.ans, sep='\n')


S = A + B + C
if S == 0:
    print('No')
elif S == 1:
    solve1([A, B, C])
elif S == 2:
    solve2([A, B, C])
else:
    solve3([A, B, C])
