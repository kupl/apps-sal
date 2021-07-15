N = int(input())
h = list(map(int, input().split()))
max_ = 100*50
h = [0] + h + [0]
cnt = 0
if max(h) == 0:
    print((0))
    return
for _ in range(max_):
    for i in range(1, N+1):
        if h[i] == 0 and h[i-1] != 0:
            cnt += 1
            break
        if h[i] > 0:
            h[i] -= 1
            if h[i] == 0 and h[i+1] == 0:
                cnt += 1
                break
        if i == N:
            cnt += 1
            break
    if sum(h) == 0:
        break
print(cnt)

