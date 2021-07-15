
N = int(input())
p = list(map(int, input().split()))

cnt = 0

for i in range(len(p)):
    if p[i] == i+1:
        if p[i] == N:
            p[i-1], p[i] = p[i], p[i-1]
        else:
            p[i], p[i+1] = p[i+1], p[i]
        cnt += 1

print(cnt)

