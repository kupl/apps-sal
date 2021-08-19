n = int(input())
ans = 0
score = []
for i in range(1, n + 1, 2):
    li = []
    for j in range(1, n + 1):
        if i % j == 0:
            li.append(j)
    if len(li) == 8:
        score.append(i)
long = len(score)
print(long)
