n = int(input())
d, x = map(int, input().split())
A = [int(input()) for _ in range(n)]

cnt = 0
for a in A:
    for i in range(d):
        tmp = i * a + 1
        if tmp > d:
            break
        cnt += 1
print(cnt + x)
