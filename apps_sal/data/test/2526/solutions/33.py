(x, y, a, b, c) = list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
q = [0] + list(map(int, input().split()))
r = [0] + list(map(int, input().split()))
p.sort()
q.sort()
r.sort()
ans = 0
num = x + y
for _ in range(num):
    if x > 0 and y > 0:
        (i, j, k) = (p[-1], q[-1], r[-1])
        if i >= j and i >= k:
            ans += i
            p.pop()
            x -= 1
        elif j >= i and j >= k:
            ans += j
            q.pop()
            y -= 1
        else:
            ans += k
            r.pop()
    elif x > 0:
        (i, j) = (p[-1], r[-1])
        x -= 1
        if i >= j:
            ans += i
            p.pop()
        else:
            ans += j
            r.pop()
    elif y > 0:
        y -= 1
        (i, j) = (q[-1], r[-1])
        if i >= j:
            ans += i
            q.pop()
        else:
            ans += j
            r.pop()
print(ans)
