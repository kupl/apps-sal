s = input().split()
n = int(s[0]); k = int(s[1])
s = input().split()
a = [1]
for i in range(1, n + 1):
    a.append(int(s[i - 1]))

for i in range(1, n + 1):
    if (a[i] >= k):
        print((0)); return


def C(nn, kk):
    nonlocal k
    prod = 1
    kk = min(kk, nn - kk)
    # print(nn, nn - kk + 1)
    for i in range(1, kk + 1):
        # print("///" + str(i))
        prod *= nn - i + 1
        prod = prod // i
        if (prod >= k):
            return -1
    if (prod >= k):
        return -1
    return prod


def holyshit(pwr):
    nonlocal n, k, a
    sum = 0
    for i in range(n, 0, -1):
        if (a[i] == 0):
            continue
        prod = C(pwr - 1 + n - i, pwr - 1)
        if (prod == -1):
            return True
        sum += prod * a[i]
        if (sum >= k):
            return True
    # print("wait, the sum is..." + str(sum))
    return False


left = 1; right = int(1e19); ans = int(1e19)
while left <= right:
    mid = (left + right) >> 1
    # print("/" + str(left) + " " + str(mid) + " " + str(right))
    if (holyshit(mid)):
        # print("////okay")
        ans = mid
        right = mid - 1
    else:
        # print("////notokay")
        left = mid + 1
print(ans)
# print(int(1e19))
# k = int(1e18)
# # print(C(6, 3))
# # print(C(10, 1))
# # print(C(7, 5))
# # print(C(8, 2))
