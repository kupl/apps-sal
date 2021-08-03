h, w = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))
ans = [[0] * w for _ in range(h)]
num = -1
for i in range(n):
    for j in range(a[i]):
        num += 1
        if (num // h) % 2 == 1:
            ans[h - 1 - num % h][num // h] = i + 1
        else:
            ans[num % h][num // h] = i + 1
for i in range(h):
    print((*ans[i]))
