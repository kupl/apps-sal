from heapq import heappush, heappop

n = int(input())
heap = []
ans = 0
last_added = []
for i in range(2 * n):
    c = input()
    if c == "remove":
        out = heappop(heap)
        if len(last_added):
            if out != last_added[-1]:
                ans += 1
                last_added = []
            else:
                last_added.pop()
    else:
        b = int(c.split()[1])
        last_added.append(b)
        heappush(heap, b)
print(ans)
