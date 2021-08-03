import sys
sys.setrecursionlimit(10**7)

n = int(input())


def search(x, use, cnt):
    if x > n:
        return
    if use == 0b111:
        cnt.append(1)

    search(x * 10 + 3, use | 0b100, cnt)
    search(x * 10 + 5, use | 0b010, cnt)
    search(x * 10 + 7, use | 0b001, cnt)


res = []
search(0, 0, res)
print(sum(res))
