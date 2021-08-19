def to_str(arr):
    if arr == -1:
        return -1
    for i in range(len(arr)):
        arr[i] = str(arr[i])
    return ' '.join(arr)


def get_seq(n, k, mult=1):
    if n < round(k * (k + 1) / 2):
        return -1
    ans = []
    for i in range(k):
        ans.append((i + 1) * mult)
    ans[k - 1] = (n - round(k * (k - 1) / 2)) * mult
    return ans


def get_seq_new(n, k):
    if n < round(k * (k + 1) / 2):
        return -1
    pre_val = []
    for num in range(2, round(n ** 0.5) + 1):
        if n % num == 0:
            if num >= round(k * (k + 1) / 2):
                return get_seq(num, k, round(n / num))
            if round(n / num) >= round(k * (k + 1) / 2):
                pre_val = get_seq(round(n / num), k, num)
    if len(pre_val) > 0:
        return pre_val
    return get_seq(n, k)


s = input()
n = int(s.split(' ')[0])
k = int(s.split(' ')[1])
print(to_str(get_seq_new(n, k)))
