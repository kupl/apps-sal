n = int(input())
a = list(map(int, input().split()))
l = []
for i in a:
    cnt = 0
    while i % 2 == 0:
        cnt += 1
        i //= 2
    l.append(cnt)
print(min(l))
