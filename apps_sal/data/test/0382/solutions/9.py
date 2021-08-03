n, m, q = list(map(int, input().split()))
s = input()
t = input()
arr = [0] * n
for i in range(n - m + 1):
    if t == s[i:i + m]:
        arr[i] = 1
    if i:
        arr[i] += arr[i - 1]
for i in range(q):
    l, r = list(map(int, input().split()))
    l -= 1
    r -= 1
    L = l - 1
    R = r - m + 1
    if R < L:
        print(0)
        continue
    if L >= 0:
        print(arr[R] - arr[L])
    else:
        print(arr[R])
