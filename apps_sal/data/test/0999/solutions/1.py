from operator import itemgetter
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
m = int(input())
b = [list(map(int, input().split())) for i in range(m)]
am = min(a, key=itemgetter(1))[1]
ap = max(a, key=itemgetter(0))[0]
bm = min(b, key=itemgetter(1))[1]
bp = max(b, key=itemgetter(0))[0]
ab = max(ap - bm, 0)
ba = max(bp - am, 0)
print(max(ab, ba))
