n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt, temp = 0, a[0]
head, tail = 1, 0
while tail < n:
    if head < n:
        if temp + a[head] < k:
            temp += a[head]
            head += 1
        else:
            if temp < k:
                cnt += head - tail
            temp -= a[tail]
            tail += 1
            if tail == head:
                temp += a[head]
                head += 1
    else:
        if temp < k:
            cnt += head - tail
        tail += 1
print((n + 1) * n // 2 - cnt)
