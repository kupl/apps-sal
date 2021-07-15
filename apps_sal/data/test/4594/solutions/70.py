N = int(input())
d = []
for i in range(N):
    d.append(int(input()))
cnt = 0
for i in range(1,101):
    qual = 0
    for j in d:
        if i == j:
            qual = 1
    if qual == 1:
        cnt += 1
print(cnt)
