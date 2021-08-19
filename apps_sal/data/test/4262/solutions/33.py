n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
queue = [[]]
lst = []
while queue:
    e = queue.pop(-1)
    if len(e) == n:
        lst.append(tuple(e))
        continue
    for i in range(1, n + 1):
        if i not in e:
            queue.append(e + [i])
lst.sort()
print(abs(lst.index(P) - lst.index(Q)))
