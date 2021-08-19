def Check(target, rest, table):
    b = [0] * n
    delta = 0
    for i in range(n):
        if b[i] < 0:
            delta += b[i]
        if table[i] + delta < target:
            sub = target - table[i] - delta
            rest -= sub
            if rest < 0:
                return False
            delta += sub
            if i + w < n:
                b[i + w] -= sub
    return True


(n, m, w) = list(map(int, input().split()))
a = list(map(int, input().split()))
head = min(a)
tail = head + m
ans = head
while head <= tail:
    mid = (head + tail) // 2
    if Check(mid, m, a):
        ans = mid
        head = mid + 1
    else:
        tail = mid - 1
print(ans)
