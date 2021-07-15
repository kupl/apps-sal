inp = input().split(" ")
for i in range(len(inp)):
    inp[i] = int(inp[i])
n, h, a, b, k = inp
queries = []
for i in range(k):
    q = input().split(" ")
    for i in range(len(q)):
        q[i] = int(q[i])
    queries.append(q)
for query in queries:
    t1, f1, t2, f2 = query
    distance = abs(t2 - t1)
    if a <= f1 <= b or t1 == t2:
        distance += abs(f2 - f1)
    elif f1 < a:
        distance += (a - f1) + abs(f2 - a)
    else: # f2 > b:
        distance += (f1 - b) + abs(f2 - b)
    print(distance)

