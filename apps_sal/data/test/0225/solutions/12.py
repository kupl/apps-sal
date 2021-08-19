__author__ = 'Esfandiar'
'\nimport sys\ninput=sys.stdin.readline\nn = int(input())\nmap(int,input().split())\nlist(map(int,input().split()))\n'
a = sorted(list(map(int, input().split())))
if a[0] + a[-1] == a[1] + a[-2] or a[0] + a[1] + a[2] == a[3]:
    print('YES')
else:
    print('NO')
