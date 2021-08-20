N = int(input())
li = [list(map(int, input().split())) for _ in range(N - 1)]
for i in range(N - 1):
    (ci, si, fi) = li[i]
    time = si + ci
    for j in range(i + 1, N - 1):
        (cj, sj, fj) = li[j]
        if time % fj != 0:
            time = (time // fj + 1) * fj
        if time < sj:
            time = sj
        time += cj
    print(time)
print(0)
