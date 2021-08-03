def mult_input():
    return map(int, input().split())


def list_input():
    return list(map(int, input().split()))


for nt in range(int(input())):
    n, k = mult_input()
    l = list(map(int, input().split()))
    ans = 0
    for i in range(1, k - 1):
        if l[i] > l[i - 1] and l[i] > l[i + 1]:
            ans += 1
    ind = 1
    i = 1
    count = ans
    while i < n - k + 1:
        if l[i] > l[i - 1] and l[i] > l[i + 1]:
            count -= 1
        if l[i + k - 2] > l[i + k - 3] and l[i + k - 2] > l[i + k - 1]:
            count += 1
        if count > ans:
            ans = count
            ind = i + 1
        i += 1
    print(ans + 1, ind)
