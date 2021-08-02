N = int(input())
a = list(map(int, input().split()))
cnt = 0
for x in a:
    while x % 2 == 0:
        x //= 2
        cnt += 1
print(cnt)
