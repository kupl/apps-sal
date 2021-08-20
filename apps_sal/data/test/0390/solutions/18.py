(n, a, b) = map(int, input().split())
c = list(map(int, input().split()))
m = min(a, b)
cnt = 0
if n % 2 == 1:
    if c[n // 2] == 2:
        cnt += m
for i in range(n // 2):
    left = c[i]
    right = c[-i - 1]
    if left == 0 and right == 1 or (left == 1 and right == 0):
        cnt = -1
        break
    else:
        if left != right:
            if left == 2:
                if right == 0:
                    cnt += a
                else:
                    cnt += b
            elif left == 0:
                cnt += a
            else:
                cnt += b
        if left == right:
            if left == 2:
                cnt += 2 * m
print(cnt)
