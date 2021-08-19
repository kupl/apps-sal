def ask(x):
    s = {}
    s[0] = 1
    (sum, cnt, res) = (0, 0, 0)
    for i in range(n):
        if a[i] < x:
            sum -= 1
            cnt -= s.get(sum, 0)
        else:
            cnt += s.get(sum, 0)
            sum += 1
        s[sum] = s.get(sum, 0) + 1
        res += cnt
    return res


(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
print(ask(m) - ask(m + 1))
