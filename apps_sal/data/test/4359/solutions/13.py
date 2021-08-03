import itertools
A = []
for i in range(5):
    A.append(int(input()))
per = list(itertools.permutations(range(5)))
ans = []
check = 0
for k in per:
    time = 0
    for i in range(5):
        s = k[i]
        time += A[s]
        temp = time // 10
        if time % 10 != 0 and i != 4:
            time = (temp + 1) * 10
    ans.append(time)
print(min(ans))
