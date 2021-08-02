import collections
def i_input(): return int(input())


def i_map(): return list(map(int, input().split()))


def i_list(): return list(map(int, input().split()))


def i_row(N): return [int(input()) for _ in range(N)]


def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


n = i_input()
ss = [input() for _ in range(n)]
ss.sort()
c = collections.Counter()
for word in ss:
    c[word] += 1

prtcnt = max(c.values())
for word, cnt in list(c.items()):
    if cnt == prtcnt:
        print(word)
