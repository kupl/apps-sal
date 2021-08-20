k = int(input())
while k:
    k -= 1
    n = int(input())
    (*a,) = map(int, input().split())
    a = sorted(a, reverse=True)
    cnt = 0
    for i in range(n):
        if i + 1 <= a[i]:
            cnt += 1
    print(cnt)
