N = int(input())
texts = [0] * N
texts = input().split()
ends = set()
ends.add(0)
for i in range(N):
    if int(texts[i]) in ends:
        ends.remove(int(texts[i]))
    ends.add(i + 1)
print(len(ends))
