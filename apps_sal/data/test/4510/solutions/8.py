from collections import deque
(n, k) = map(int, input().split())
a = [int(i) for i in input().split()]
now = set()
letters = deque()
for i in range(n):
    if a[i] not in now:
        now.add(a[i])
        if len(letters) < k:
            letters.append(a[i])
        else:
            now.remove(letters.popleft())
            letters.append(a[i])
print(len(letters))
print(*list(letters)[::-1])
