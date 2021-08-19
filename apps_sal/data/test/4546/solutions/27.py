# 柱の高さa,b,cがb-a=c-bを満たすか

a, b, c = map(int, input().split())

if b - a == c - b:
    print('YES')
else:
    print('NO')
