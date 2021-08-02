import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

LIST = [[] for i in range(n + 1)]

for i in range(n):
    LIST[n - A[i]].append(i)

ANSLIST = [None] * (n + 1)
h = 1
for i in range(1, n + 1):
    if len(LIST[i]) % i != 0:
        print("Impossible")
        return

    else:
        j = 0
        while j < len(LIST[i]):
            ANSLIST[LIST[i][j]] = h
            j += 1
            if j % i == 0:
                h += 1

print("Possible")
for a in ANSLIST[:-1]:
    print(a, end=" ")
