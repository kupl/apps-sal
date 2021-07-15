n, s = map(int, input().split())
num = list(map(int, input().split()))
x = sum(num)
if x < s:
    print(-1)
else:
    k = min(num)
    for i in range(n):
        s -= abs(num[i] - k)
        num[i] = k
    if s <= 0:
        print(k)
    else:
        q = s // n
        k -= q
        if s % n == 0:
            print(k)
        else:
            print(k - 1)
