t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    cnt = 0
    while n != 0:
        cnt += n % k
        n //= k
        cnt += 1
    print(cnt - 1)
