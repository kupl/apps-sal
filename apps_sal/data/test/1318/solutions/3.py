import sys


class Visitor():
    def __init__(self, pi, ci, i):
        self.ci = ci
        self.pi = pi
        self.i = i
        self.place = None

    def __repr__(self):
        return "{} {} {}".format(self.ci, self.pi, self.i)


class Place():
    def __init__(self, i, max_):
        self.i = i
        self.max_ = int(max_)

    def __repr__(self):
        return "{} {}".format(self.max_, self.i)


def __starting_point():
    lines = sys.stdin.readlines()
    n = int(lines[0])
    visitors = []
    for i in range(1, n + 1):
        ci, pi = lines[i].split()
        visitors.append(Visitor(int(pi), int(ci), i))

    places = []
    for i, place in enumerate(lines[n + 2].split()):
        places.append(Place(i + 1, place))

    visitors = sorted(visitors, key=lambda x: x.pi)[::-1]
    places = sorted(places, key=lambda x: x.max_)

    visited = [None for _ in places]
    total = 0
    for visitor in visitors:
        for i, place in enumerate(places):
            if visitor.ci <= place.max_ and visited[i] is None:
                visited[i] = visitor
                visitor.place = place
                total += visitor.pi
                break

    new_visitors = list([x for x in sorted(visitors, key=lambda x: x.i) if x.place is not None])
    print("{} {}".format(len(new_visitors), total))
    for visitor in new_visitors:
        print("{} {}".format(visitor.i, visitor.place.i))


__starting_point()
