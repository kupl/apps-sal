h, w = list(map(int, input().split()))
c = [list(input()) for _ in range(h)]
cc = [[] for i in range(2 * h)]
for i in range(h):
    cc[2 * i].append(c[i])
    print(("".join(*cc[2 * i])))
    cc[2 * i + 1].append(c[i])
    print(("".join(*cc[2 * i + 1])))
