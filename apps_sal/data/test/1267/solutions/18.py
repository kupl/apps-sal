

n = int(input())
a = set(map(int, input().split()))


cnt = 0
for i in a:
    if i > 0:
        cnt += 1

print(cnt)
