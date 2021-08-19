import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
PLACE = [None] * (n + 1)
for i in range(n):
    PLACE[A[i]] = i

al = n


WINLIST = [None] * (n + 1)  # 0:そこに行けば必敗,1:そこにいけば必勝


def move(n, al):
    place = PLACE[n]
    for i in range(place, -1, -n):
        if A[i] > n and WINLIST[A[i]] == "B":
            WINLIST[n] = "A"
            return

    for i in range(place, al, n):
        if A[i] > n and WINLIST[A[i]] == "B":
            WINLIST[n] = "A"
            return

    else:
        WINLIST[n] = "B"
        return


for j in range(n, 0, -1):
    move(j, al)


ANS = ""
for i in A:
    ANS += WINLIST[i]

print(ANS)
