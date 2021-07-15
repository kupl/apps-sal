def read_int():
    return int(input())


def read_ints():
    return list(map(int, input().split(' ')))


t = read_int()
for case_num in range(t):
    n = read_int()
    a = list(read_ints())
    cnt = [0 for _ in range(101)]
    for i in a:
        cnt[i] += 1
    ans = 0
    status = 2
    for i in range(101):
        status = min(status, cnt[i])
        if status == 0:
            break
        ans += status
    print(ans)

