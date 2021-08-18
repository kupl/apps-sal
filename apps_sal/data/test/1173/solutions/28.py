import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())

A = [None] * N
for i in range(N):
    A[i] = [-1] + [int(x) - 1 for x in input().split()[::-1]]


def f(candi):

    played = []

    for n in candi:
        target = A[n][-1]
        if A[target][-1] == n:
            played.append(n)

    new_candi = set()
    for n in played:
        A[n].pop()
        new_candi.add(n)
        if A[n][-1] != -1:
            new_candi.add(A[n][-1])

    return len(played), new_candi


answer = 0
rest = N * (N - 1)
play_candi = set(range(N))

while True:
    answer += 1
    x, play_candi = f(play_candi)
    if x == 0:
        answer = -1
        break

    rest -= x
    if rest == 0:
        break

print(answer)
