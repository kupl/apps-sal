n = int(input())
a = [0] + list(map(int, input().split()))
s, f = list(map(int, input().split()))

w = f - s
max_s = cur_s = sum(a[s:f])
max_h = cur_h = s

for i in range(2, n + 1):
    cur_h -= 1
    if cur_h == 0:
        cur_h = n
    j = i + w - 1
    if j > n:
        j -= n
    cur_s = cur_s - a[i - 1] + a[j]
    if (cur_s > max_s) or (cur_s == max_s and cur_h < max_h):
        max_s = cur_s
        max_h = cur_h

print(max_h)
