n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    while i % 2 == 0:
        i = i/2
        cnt += 1
print(cnt)

