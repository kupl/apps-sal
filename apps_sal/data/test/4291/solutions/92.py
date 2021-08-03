n, q = map(int, input().split())
s = input()
a = [0] * n
for i in range(n):
    if s[i - 1] == "A" and s[i] == "C":
        a[i] = a[i - 1] + 1
    else:
        a[i] = a[i - 1]
for i in range(q):
    l, r = map(int, input().split())
    print(a[r - 1] - a[l - 1])
