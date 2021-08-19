import sys
sys.setrecursionlimit(10 ** 7)
n = int(input())
cnt = []


def search(x, use):
    if x > n:
        return
    if use == 7:
        cnt.append(1)
    search(x * 10 + 3, use | 4)
    search(x * 10 + 5, use | 2)
    search(x * 10 + 7, use | 1)


search(0, 0)
print(sum(cnt))
