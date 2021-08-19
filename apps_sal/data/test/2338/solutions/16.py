import sys
input = sys.stdin.readline
n = int(input())
bombs = [list(map(int, input().split(' '))) for _ in range(n)]
bombs.sort(key=lambda x: abs(x[0]) + abs(x[1]))
out = []
for b in bombs:
    x = b
    get = []
    back = []
    if x[0] != 0:
        get.append('1 ' + str(abs(x[0])) + ' ' + ('R' if x[0] > 0 else 'L'))
        back.append('1 ' + str(abs(x[0])) + ' ' + ('L' if x[0] > 0 else 'R'))
    if x[1] != 0:
        get.append('1 ' + str(abs(x[1])) + ' ' + ('U' if x[1] > 0 else 'D'))
        back.append('1 ' + str(abs(x[1])) + ' ' + ('D' if x[1] > 0 else 'U'))
    out.extend(get + ['2'] + back + ['3'])
sys.stdout.write('\n'.join([str(len(out))] + out))
