def rui_sum(n, k):
    k_lsum = (k - 1) * k // 2
    k_usum = k * n - (k - 1) * k // 2
    return k_usum - k_lsum + 1


(n, k) = map(int, input().split())
cnt = []
for i in range(k, n + 2):
    cnt.append(rui_sum(n, i))
print(sum(cnt) % (10 ** 9 + 7))
