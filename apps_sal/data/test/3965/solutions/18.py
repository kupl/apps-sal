import sys
n = int(input())
a = list(map(int, input().split()))
ans = True
for s in sys.stdin:
    cnt = 0
    for c in 'aeiouy':
        cnt += s.count(c)
    ans &= cnt == a.pop(0)
print('YES' if ans else 'NO')
