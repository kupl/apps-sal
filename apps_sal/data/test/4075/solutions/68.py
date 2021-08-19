import sys
input = sys.stdin.readline


def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


def LI():
    return list(map(int, input().split()))


(n, m) = MI()
sws = []
for i in range(m):
    sws.append(list(map(int, input().split())))
ps = LI()
ans = 0
for i in range(2 ** n):
    count = 0
    for j in range(m):
        sm = 0
        for k in range(1, len(sws[j])):
            sm += (i >> sws[j][k] - 1) % 2
        if sm % 2 == ps[j]:
            count += 1
    if count == m:
        ans += 1
print(ans)
