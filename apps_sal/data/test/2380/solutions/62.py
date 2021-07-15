from collections import deque

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
a = deque(a)
l = []
ans = []

for i in range(m):
    b, c = map(int, input().split())
    l.append([c, b])

l = sorted(l)[::-1]
ref = a.popleft()

for num, cnt in l:
    while ref >= num:
        ans.append(ref)
        if len(a) == 0:
            print(sum(ans))
            return
        ref = a.popleft()

    while cnt > 0:
        if ref < num:
            ans.append(num)
            cnt -= 1
            if len(a) == 0:
                print(sum(ans))
                return
            ref = a.popleft()
        else:
            break

ans.append(ref)

while a:
    ref = a.popleft()
    ans.append(ref)

print(sum(ans))
