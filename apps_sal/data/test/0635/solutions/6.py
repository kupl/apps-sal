import sys
input = sys.stdin.readline
(n, s) = map(int, input().split())
fw = [0] + list(map(int, input().split()))
bw = [0] + list(map(int, input().split()))
if fw[1] == 0:
    print('NO')
elif fw[s] == 0 and bw[s] == 0:
    print('NO')
elif fw[s] == 1:
    print('YES')
else:
    valid = False
    for i in range(s + 1, len(fw)):
        if fw[i] and bw[i]:
            valid = True
    if valid:
        print('YES')
    else:
        print('NO')
