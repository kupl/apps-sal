n = int(input())
a = [int(x) for x in input().split()]
a.sort()
(pile, tc) = (0, n)
visited = [0] * n
while tc != 0:
    tt = 0
    for i in range(0, n):
        if a[i] >= tt and visited[i] != 1:
            visited[i] = 1
            tt += 1
            tc -= 1
    if tt > 0:
        pile += 1
print(pile)
