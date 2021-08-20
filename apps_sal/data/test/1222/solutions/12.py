import collections
K = int(input())
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
deq = collections.deque(ls)
i = 0
while i != K:
    x = deq.popleft()
    if x % 10 != 0:
        deq.append(10 * x + x % 10 - 1)
    deq.append(10 * x + x % 10)
    if x % 10 != 9:
        deq.append(10 * x + x % 10 + 1)
    i += 1
print(x)
