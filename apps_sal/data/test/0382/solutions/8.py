n, m, q = map(int, input().split())
s = input()
t = input()
arr = []
for i in range(n - m + 1):
    if s[i:i + m] == t:
        arr.append(i)
for i in range(q):
    l, r = map(int, input().split())
    k = 0
    for j in range(len(arr)):
        if arr[j] >= l - 1 and arr[j] + m - 1<= r - 1:
            k = k + 1
    print(k)
