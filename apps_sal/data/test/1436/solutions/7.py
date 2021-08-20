need_log = False


def log(*s):
    if need_log:
        print(*s)


n = int(input())
a = list(map(int, input().split()))
x = 0
y = 0
for k in a:
    if k == -1:
        if y == 0:
            x += 1
        else:
            y -= 1
    else:
        y += k
print(x)
