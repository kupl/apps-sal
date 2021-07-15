import sys

n, h = map(int, input().split())
a = [list(map(int, x.split())) for x in sys.stdin.readlines()]
a.sort(reverse=True)
b = sorted(a, key=lambda x:x[1], reverse=True)
cnt = 0
for i in b:
    if i[1] < a[0][0]:
        break
    cnt += 1
    h -= i[1]
    if h <= 0:
        print(cnt)
        return
print(cnt + -(-h//a[0][0]))
