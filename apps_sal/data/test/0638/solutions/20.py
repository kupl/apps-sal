n, M = map(int, input().split())
t = list(map(int, input().split()))

prefix_sum = 0
for i in range(n):
    max_ = M - t[i]
    
    cur_sum = prefix_sum
    prefix_t = sorted(t[:i], reverse=True)
    cnt = 0
    while cur_sum > max_:
        cur_sum -= prefix_t[cnt]
        cnt += 1
    print(cnt, end=" ")
    prefix_sum += t[i]
