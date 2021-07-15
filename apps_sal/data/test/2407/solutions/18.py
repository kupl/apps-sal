from sys import stdin
input = stdin.readline
q = int(input())

for _ in range(q):
    n, r = list(map(int, input().split()))

    x = list(map(int, input().split()))
    x.sort(reverse=True)
    knockbacks = []

    for i in range(len(x)):
        if i == 0 or x[i] != x[i - 1]:
            loc = x[i]
            knockbacks.append((loc + r - 1) // r)
    
    cnt = 0
    while True:
        if cnt >= len(knockbacks) or knockbacks[cnt] <= cnt:
            break
        else:
            cnt += 1

    print(cnt)

