n = int(input())
(d, x) = map(int, input().split())
cnt = n
for i in range(n):
    a = int(input())
    b = a + 1
    while b <= d:
        cnt += 1
        b += a
print(cnt + x)
