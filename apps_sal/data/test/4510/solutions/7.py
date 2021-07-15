n, k = map(int, input().split())
a = [*map(int, input().split())]

from collections import deque

ans = deque()
ins = set()

for i in a:
	if i not in ins:
		if len(ans) == k:
			ins.remove(ans[0])
			ans.popleft()
		ans.append(i)
		ins.add(i)

ans.reverse()

print(len(ans))

print(*ans)
