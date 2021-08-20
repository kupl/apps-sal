from collections import Counter as c


def mi():
    return list(map(int, input().split()))


'\n3\naa\nabacaba\nxdd\n'
for _ in range(int(input())):
    li = list(input())
    s = c(li)
    if len(s) == 1:
        print(-1)
    else:
        print(''.join(sorted(li)))
