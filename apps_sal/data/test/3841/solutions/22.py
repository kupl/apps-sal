p, k = list(map(int, input().split()))
a = ''
cnt = 0
while p != 0:
    cnt += 1
    a += str(p % k) + ' '
    p -= p % k
    p //= -k
print(cnt)
print(a)


