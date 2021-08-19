import sys
ioRead = sys.stdin.readline
def ioWrite(x): return sys.stdout.write(f"{x}\n")


n, m, q = map(int, ioRead().split(" "))
rows_and_columns = n + m
seen = [False for _ in range(rows_and_columns)]
connectsTo = [[] for _ in range(rows_and_columns)]

for _ in range(q):
    r, c = map(lambda x: int(x) - 1, ioRead().split(" "))
    c += n
    connectsTo[r].append(c)
    connectsTo[c].append(r)

inserts = -1
for i in range(rows_and_columns):
    if not seen[i]:
        inserts += 1
        stack = [i]
        while stack:  # BFS
            current = stack.pop()
            if not seen[current]:
                seen[current] = True
                for n in connectsTo[current]:
                    if not seen[n]:
                        stack.append(n)

ioWrite(inserts)
