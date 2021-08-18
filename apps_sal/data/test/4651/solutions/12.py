ct = int(input())
for c in range(ct):
    n = int(input())
    li = [int(i) for i in input().split()]

    op = [0 for i in range(n)]
    for i in range(1, n + 1):
        pos = li.index(i)
        for j in range(pos - 1, -1, -1):
            if op[j] == 0 and li[j] > li[j + 1]:
                op[j] = 1
                li[j], li[j + 1] = li[j + 1], li[j]
            else:
                break
    print(*li)
