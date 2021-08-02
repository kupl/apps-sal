n, k = map(int, input().split())
a = map(int, input().split())
b = [0] * n
for i, p in enumerate(a):
    cur_start = max(0, i - k)
    cur_end = min(n - 1, i + k)
    if p == 0:
        b[i] = cur_end - cur_start + 1
    else:
        p -= 1
        prev_end = min(n - 1, p + k)
        if cur_start > prev_end:
            b[i] = b[p] + cur_end - cur_start + 1
        else:
            b[i] = b[p] + cur_end - prev_end

print(' '.join(map(str, b)))
