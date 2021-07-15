n = int(input())


def _kakko(s):
    l, lr = 0, 0
    for c in s:
        if c == ')':
            if lr == 0:
                l = l + 1
            else:
                lr = lr - 1
        else:
            lr = lr + 1
    return (l, lr)


s = [_kakko(input()) for _ in range(n)]

sl = [ss for ss in s if ss[1] >= ss[0]]
sr = [ss for ss in s if ss[1] < ss[0]]

sl.sort(key=lambda x: x[0])
sr.sort(key=lambda x: x[1], reverse=True)

r = 0
for ss in sl:
    if ss[0] > r:
        print('No')
        return
    r = r + ss[1] - ss[0]

for ss in sr:
    if ss[0] > r:
        print('No')
        return
    r = r + ss[1] - ss[0]

if r != 0:
    print('No')
    return

print('Yes')

