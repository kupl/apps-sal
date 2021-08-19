def rint():
    return int(input())


def rmint():
    return map(int, input().split())


def rlist():
    return list(rmint())


n = rint()
lst = rlist()
cnt = {}
for nb in lst:
    if nb not in cnt:
        cnt[nb] = 1
    else:
        cnt[nb] += 1
arr = sorted(list(cnt.keys()))
N = len(arr)
(left, right, k) = (0, 0, cnt[arr[0]])
(left_best, right_best, k_best) = (0, 0, cnt[arr[0]])
while right < N:
    while right + 1 < N and arr[right + 1] == arr[right] + 1 and (cnt[arr[right]] >= 2):
        right = right + 1
        k += cnt[arr[right]]
    if k_best < k:
        (left_best, right_best, k_best) = (left, right, k)
    if right + 1 >= N:
        break
    elif arr[right + 1] != arr[right] + 1:
        left = right + 1
        right = right + 1
        k = cnt[arr[left]]
    else:
        left = right
        right = right + 1
        k = cnt[arr[left]] + cnt[arr[right]]
print(k_best)
for idx in range(left_best, right_best + 1):
    print((str(arr[idx]) + ' ') * (cnt[arr[idx]] - 1), end='')
for idx in range(right_best, left_best - 1, -1):
    print(str(arr[idx]) + ' ', end='')
print('')
