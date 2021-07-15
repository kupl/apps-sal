import heapq

a = []
h = []
heapq.heapify(h)

for _ in range(int(input())):
    l = input()

    if l.startswith("insert"):
        heapq.heappush(h, int(l.split()[1]))

    elif l.startswith("getMin"):
        m = int(l.split()[1])
        while len(h) > 0 and h[0] != m:
            if h[0] < m:
                heapq.heappop(h)
                a.append("removeMin")
            else:
                heapq.heappush(h, m)
                a.append("insert " + str(m))
        if len(h) == 0:
            heapq.heappush(h, m)
            a.append("insert " + str(m))

    elif l.startswith("removeMin"):
        if len(h) == 0:
            a.append("insert 1")
        else:
            heapq.heappop(h)

    a.append(l)

print(len(a))
print("\n".join(a))
