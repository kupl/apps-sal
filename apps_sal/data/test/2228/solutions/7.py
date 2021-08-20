n = int(input())
l1 = []
l2 = []
for i in range(n):
    (a, b) = map(int, input().split())
    l1.append(a)
    l2.append(b)
l1.sort(reverse=True)
l2.sort(reverse=True)
cur = 0
mx = 0
ans = 0
while l1:
    if l1[-1] < l2[-1]:
        t = l1.pop()
        cur += 1
        if cur > mx:
            mx = cur
            ans = t
    else:
        l2.pop()
        cur -= 1
print(ans, mx)
