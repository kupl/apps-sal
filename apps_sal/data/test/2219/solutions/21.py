t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    count = 0
    while n != 0:
        if n % k == 0:
            n//=k
            count += 1
        else:
            count += n%k
            n -= n%k
    print(count)
