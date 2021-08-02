import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readlines


def main():

    lines = input()
    n = int(lines[0].strip())

    E = [list(map(int, lines[i].split())) for i in range(1, n + 1)]
    E = sorted(E, key=lambda x: x[1])

    cur_t = 0

    for i in range(n):
        cur_t += E[i][0]
        if cur_t > E[i][1]:
            print('No')
            return

    print('Yes')


main()
