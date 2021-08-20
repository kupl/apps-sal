n = int(input())
(d, x) = map(int, input().split())
a = [int(input()) for _ in range(n)]
cnt = x
for q in a:
    cnt += (d + q - 1) // q
print(cnt)
