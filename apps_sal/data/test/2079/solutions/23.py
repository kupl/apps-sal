import heapq
n = int(input())

w = list(map(int, input().split()))
for i, ww in enumerate(w):
    w[i] = (ww, i + 1)
p = input()

w = sorted(w)
que = []

t = 0
ans = []

for s in p:
    if s == '0':
        heapq.heappush(que, w[t])
        ans.append(w[t][1])
        t += 1
    else:
        head = que.pop()

        ans.append(head[1])

print(*ans)
