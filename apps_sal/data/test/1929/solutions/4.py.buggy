need_log = False


def log(*s):
    if need_log:
        print(*s)


n, t, c = map(int, input().split())
a = list(map(int, input().split()))

if c == 0:
    print(0)
    return

g = []
k = 0
for i in a:
    if i <= t:
        k += 1
    elif k > 0:
        g += [k]
        k = 0
if k > 0:
    g += [k]
log(g)

result = 0

for i in g:
    result += max(i - c + 1, 0)

print(result)
