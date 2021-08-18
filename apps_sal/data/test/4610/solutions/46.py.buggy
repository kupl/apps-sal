from collections import Counter, deque, defaultdict
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
t = defaultdict(int)
for x in A:
    t[x] += 1
B = list(t.values())
B.sort()
if(len(B) <= k):
    print((0))
    return

ans = sum(B[:len(B) - k])
print(ans)
