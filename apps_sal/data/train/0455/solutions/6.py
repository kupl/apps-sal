
def walk(grid):
    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            yield ((i, j), elem)


def extend(bound, ij):
    i, j = ij
    if bound is None:
        return (ij, ij)
    else:
        ((i0, j0), (i1, j1)) = bound
        return (
            (min(i0, i), min(j0, j)),
            (max(i1, i), max(j1, j)),
        )


def contains(bound, ij):
    i, j = ij
    ((i0, j0), (i1, j1)) = bound
    return i0 <= i <= i1 and j0 <= j <= j1


def has_toposort(prereq):
    roots = [x for x in prereq if not prereq[x]]
    while roots:
        r = roots.pop()
        del prereq[r]
        for c in prereq:
            if r in prereq[c]:
                prereq[c].remove(r)
                if not prereq[c]:
                    roots.append(c)
    return not prereq


def printable(grid):
    m, n = len(grid), len(grid[0])
    assert m >= 1 and n >= 1

    colors = {c for row in grid for c in row}
    bounds = {c: None for c in colors}

    for ((i, j), c) in walk(grid):
        bounds[c] = extend(bounds[c], (i, j))

    prereq = {c: set() for c in colors}
    for ((i, j), c) in walk(grid):
        for c2 in colors:
            if c2 == c:
                continue
            if contains(bounds[c2], (i, j)):
                prereq[c].add(c2)

    return has_toposort(prereq)


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        return printable(targetGrid)
