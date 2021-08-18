
n, m = (int(x) for x in input().split())
w = [int(x) for x in input().split()]
b = [int(x) - 1 for x in input().split()]

visited = [False] * n
stack = []
for book in b:
    if not visited[book]:
        stack.append(book)
        visited[book] = True
stack.reverse()

total_weight = 0
for reading in b:
    p = len(stack) - 1
    while stack[p] != reading:
        total_weight += w[stack[p]]
        p -= 1
    else:
        stack.__delitem__(p)
        stack.append(reading)

print(total_weight)
