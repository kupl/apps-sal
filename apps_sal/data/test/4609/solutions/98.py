N = int(input())
A = [int(input()) for _ in range(N)]

paper = set()
for a in A:
    if a in paper:
        paper.remove(a)
    else:
        paper.add(a)
ans = len(paper)
print(ans)
