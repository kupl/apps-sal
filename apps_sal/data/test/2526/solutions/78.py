import heapq

X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort()

s = p[:X] + q[:Y]
ans = sum(s)
heapq.heapify(s)

while r and s:
    if s[0] < r[-1]:
        ans += r[-1]
        r.pop()
        ans -= heapq.heappop(s)
    else:
        break
print(ans)
