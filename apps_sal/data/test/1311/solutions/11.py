from sys import stdin, setrecursionlimit
import threading


def main():
    n = int(stdin.readline())
    line = []
    for i in range(n):
        (x, w) = [int(x) for x in stdin.readline().split()]
        line.append((x - w, x + w))
    line.sort()

    def best(ind, line):
        r = line[ind][1]
        nxt = ind + 1
        while nxt < len(line):
            (nL, nR) = line[nxt]
            if nL >= r:
                return best(nxt, line) + 1
            elif nR < r:
                return best(nxt, line)
            nxt += 1
        return 1
    print(best(0, line))


def __starting_point():
    setrecursionlimit(10 ** 6)
    threading.stack_size(10 ** 8)
    t = threading.Thread(target=main)
    t.start()
    t.join()


__starting_point()
