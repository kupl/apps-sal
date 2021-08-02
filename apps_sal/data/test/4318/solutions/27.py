N = int(input())
H = list(map(int, input().split()))

cnt = 0
max_ = 0
for h in H:
    if h >= max_:
        cnt += 1
        max_ = h

print(cnt)
