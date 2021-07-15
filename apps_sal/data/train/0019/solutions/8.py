import math
import collections
arrK = [0] * 1000050

def cleanK(q):
    while len(q):
        arrK[q.pop()] = 0


def test():
    n, k, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = math.inf
    q = collections.deque()
    sumK = 0
    for i in range(len(a)):
        q.append(a[i])
        if arrK[a[i]] == 0:
            sumK += 1
        arrK[a[i]] += 1

        if len(q) > d:
            var = q.popleft()
            arrK[var] -= 1
            if arrK[var] == 0:
                sumK -= 1
        if len(q) == d and sumK < ans:
            ans = sumK
    cleanK(q)
    print(ans)
#
# def print2d(a):
#     for i in a:
#       print(' '.join(list(map(str, i))))

t = int(input())

for i in range(t):
    test()
