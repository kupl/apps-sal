n = int(input())
m = list(map(int, input().split()))
r = list(map(int, input().split()))

cnt = 0
for i in range(720720):
    for j in range(n):
        if i % m[j] == r[j]:
            cnt += 1
            break

print(cnt / 720720)
