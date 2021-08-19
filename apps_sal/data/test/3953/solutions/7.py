class Solver(object):

    def read_input(self):
        n = int(input())
        grid = []
        for i in range(n):
            l = list(input())
            grid.append(l)
        self.n = n
        self.grid = grid

    def solve_line(self):
        pos = []
        for i in range(self.n):
            res = False
            for j in range(self.n):
                if self.grid[i][j] == '.':
                    res = True
                    pos.append((i, j))
                if res == True:
                    break
            if res == True:
                continue
            else:
                pos = -1
                break
        self.pos = pos
        return pos

    def solve_column(self):
        pos = []
        for j in range(self.n):
            res = False
            for i in range(self.n):
                if self.grid[i][j] == '.':
                    res = True
                    pos.append((i, j))
                if res == True:
                    break
            if res == True:
                continue
            else:
                pos = -1
                break
        self.pos = pos
        return pos

    def print_solution(self):
        for (i, j) in self.pos:
            print(i + 1, j + 1)

    def solve(self):
        lines = self.solve_line()
        if lines != -1:
            self.print_solution()
        else:
            cols = self.solve_column()
            if cols == -1:
                print(-1)
            else:
                self.print_solution()


S = Solver()
S.read_input()
S.solve()
