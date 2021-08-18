N = int(input())
A = [int(input()) for _ in range(N)]

paper = set()
for a in A:
    if not(a in paper):
        paper.add(a)
    else:
        paper.remove(a)
print(len(paper))
