n = int(input())
a = list(map(int, input().split()))
x = list(sorted(set(a)))
n_sub = n * (n + 1) // 2
Li = 0
Ri = len(x)
while Ri > Li + 1:
    i = (Li + Ri) // 2
    xi = x[i]
    UorD = [1 if ak >= xi else -1 for ak in a]
    cnt_sum = [0] * (2 * n + 1)
    cumsum = 0
    cnt_sum[cumsum + n] = 1
    judge = 0
    s = 0
    for uk in UorD:
        cumsum += uk
        if uk == 1:
            s += cnt_sum[cumsum + n] + 1
        else:
            s -= cnt_sum[cumsum + n + 1] - 1
        cnt_sum[cumsum + n] += 1
        judge += s
        if judge >= n_sub // 2:
            Li = i
            break
    else:
        Ri = i
print(x[Li])
