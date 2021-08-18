import sys
input = sys.stdin.readline
n = int(input())
L = sorted(set(map(int, input().split())))

while True:
    num = L[0]
    L = sorted(set(L[i] % L[0] for i in range(1, len(L)) if L[i] % L[0] != 0))
    L.append(num)
    L.sort()
    if len(L) <= 1:
        print((L[0]))
        return
