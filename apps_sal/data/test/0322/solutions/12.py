def read():
    return map(int, input().split())


n = int(input())
cnt1 = cnt2 = 0
for i in range(n):
    (x, y) = read()
    if x < 0:
        cnt1 += 1
    else:
        cnt2 += 1
print('Yes' if min(cnt1, cnt2) <= 1 else 'No')
