N = int(input())
ans = 0


def count_dig(N):
    cnt = 0
    while True:
        cnt += 1
        if N < 10:
            break
        else:
            N /= 10
    return cnt


for i in range(1, N + 1):
    if count_dig(i) % 2 == 1:
        ans += 1
print(ans)
