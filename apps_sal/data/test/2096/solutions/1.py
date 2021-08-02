n = int(input())
a = list(map(int, input().split()))
proc = sorted([(a.count(i), i) for i in range(10, 100) if a.count(i) > 0])
left, right = [], []
for cnt, val in proc:
    half = cnt // 2
    left.extend([val] * half)
    right.extend([val] * half)
    if cnt % 2 == 1:
        if len(left) < len(right):
            left.append(val)
        else:
            right.append(val)
print(len(set(left)) * len(set(right)))
cnt = [0 for i in range(100)]
for i in range(2 * n):
    if left.count(a[i]) == cnt[a[i]]:
        print('2', end=' ')
    else:
        print('1', end=' ')
        cnt[a[i]] += 1
