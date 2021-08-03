N = int(input())
An = list(map(int, input().split()))
An.sort(reverse=True)
answer = 0
t = N - 1
for i, Ai in enumerate(An):
    lim = 2
    if i == 0:
        lim = 1
    for j in range(lim):
        if t > 0:
            answer += Ai
        t -= 1
print(answer)
