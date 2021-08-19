n = int(input())
paper = dict()
for i in range(n):
    a = int(input())
    if a not in paper:
        paper[a] = 1
    else:
        paper.pop(a)
res = 0
for value in list(paper.values()):
    if value == 1:
        res += 1
print(res)
