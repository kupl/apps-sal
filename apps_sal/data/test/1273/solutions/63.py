from sys import setrecursionlimit


setrecursionlimit(10**6)



n = int(input())
t = [list(map(int, input().split())) for _ in range(n-1)]



hands = [0 for _ in range(n+1)]
for a, b in t:
    hands[a] += 1
    hands[b] += 1

number_of_colors = max(*hands)

def next_color(i):
    return i+1 if i < number_of_colors else 1



class edge():
    def __init__(self, en):
        self.ends = en
        self.color = 0

    def set_color(self, co):
        self.color = co

class nord():
    def __init__(self, tr):
        self.parent = tr
        self.edges = []

    def add(self, ed):
        self.edges.append(ed)

    def set_color(self, previous_color):
        co = next_color(previous_color)
        for ed in self.edges:
            if ed.color == 0:
                ed.set_color(co)
                for i in ed.ends:
                    no = self.parent.nords[i-1]
                    if self is not no:
                        no.set_color(co)
                co = next_color(co)

class tree():
    def __init__(self):
        self.nords = []

    def add_nord(self, no):
        self.nords.append(no)

    def add_edge(self, ed):
        for i in ed.ends:
            self.nords[i-1].add(ed)

    def set_color(self):
        self.nords[0].set_color(0)


tr = tree()
for _ in range(n):
    no = nord(tr)
    tr.add_nord(no)

e_tree = []
for en in t:
    ed = edge(en)
    e_tree.append(ed)
    tr.add_edge(ed)

tr.set_color()

print(number_of_colors)
for e in e_tree:
    print(e.color)
