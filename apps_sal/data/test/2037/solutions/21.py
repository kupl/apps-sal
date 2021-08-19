(N, M) = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))
problems = [0] * N
count = 0
ans = []
append = ans.append
for n in a:
    if not problems[n]:
        count += 1
    problems[n] += 1
    append(1 if count == N else 0)
    if count == N:
        count = 0
        for i in range(N):
            problems[i] -= 1
            if problems[i] > 0:
                count += 1
print(*ans, sep='')
