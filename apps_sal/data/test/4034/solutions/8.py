import sys


def main():
    n = int(sys.stdin.readline().split()[0])
    s = sys.stdin.readline().split()[0]
    color = [None] * n
    color[0] = 0
    for i in range(n):
        if color[i] == None:
            color[i] = 0
        for j in range(i + 1, n):
            if ord(s[j]) < ord(s[i]):
                if color[j] == color[i]:
                    print('NO')
                    return
                if color[j] == None:
                    color[j] = color[i] ^ 1
    print('YES')
    print(*color, sep='')


main()
