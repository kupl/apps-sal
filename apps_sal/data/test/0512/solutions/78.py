import collections
import heapq


def default():
    return -1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dica = [-1] * (2 * n + 1)
dicb = [-1] * (2 * n + 1)
cnta = collections.defaultdict(int)
cntb = collections.defaultdict(int)
for a, b in arr:
    c = b - a - 1
    if ((a != -1 and b != -1) and (a >= b or n < b - a)) or (cnta[a] == 1 or cntb[a] == 1 or cnta[b] == 1 or cntb[b] == 1):
        print('No')
        return
    if a != -1:
        cnta[a] += 1
        dica[a] = b
    if b != -1:
        cntb[b] += 1
        dicb[b] = a
flag = [True] * (2 * n + 1)
q = []
heapq.heappush(q, 1)
s = set()
s.add(1)


def judge(i, j):
    k = j - i
    for pos in range(i, j):
        a = pos
        b = pos + k
        if cnta[b] == 1 or cntb[a] == 1 or (cnta[a] == 1 and cntb[b] == 1 and dica[a] != b):
            return False
    return True


while len(q) != 0:
    i = heapq.heappop(q)
    if i == 2 * n + 1:
        print('Yes')
        return
    for j in range(i + 1, n + (i + 1) // 2 + 1):
        if judge(i, j):
            if 2 * j - i not in s:
                heapq.heappush(q, 2 * j - i)
                s.add(2 * j - i)
print('No')
return
