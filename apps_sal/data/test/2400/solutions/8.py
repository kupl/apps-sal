def get_cnt():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0, 0]
    for x in a:
        cnt[x % 2] += 1
    return cnt


for _ in range(int(input())):
    p = get_cnt()
    q = get_cnt()
    ans = p[0] * q[0] + p[1] * q[1]
    print(ans)
