def calc(ans, k, n):
    for i in range(1, len(ans)):
        if ans[i] >= n + k * (((i - k) // k) * ((i - k) // k + 1)) // 2 + ((i - k) % k) * ((i - k) // k + 1):
            #print("panne ",i,k,ans[i],(((i-k)//k)*((i-k)//k  + 1))//2 + ((i-k)%k)*((i-k)//k  + 1))
            return True

    return False


def bins(ans, n, low, high):
    if low == high and calc(ans, low, n):
        # print(low,high)
        return low
    elif low == high:
        return -1
    if calc(ans, (low + high) // 2, n):
        return bins(ans, n, low, (low + high) // 2)
    else:
        return bins(ans, n, (low + high) // 2 + 1, high)


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = [0] * (n + 1)
for i in range(1, n + 1):
    ans[i] = ans[i - 1] + a[i - 1]
# print(ans)
print(bins(ans, k, 1, n))
# print(calc(ans,7,550))
# print(ans[47])
