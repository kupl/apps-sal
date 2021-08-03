s = input()
q = int(input())
for i in range(q):
    a = list(map(int, input().split()))
    l = a[0]
    r = a[1]
    k = a[2]
    s2 = s[l - 1:r]
    n = len(s2)
    k = k % n
    ls = s2[:n - k]
    rs = s2[n - k:]
    s = s[:l - 1] + rs + ls + s[r:]
print(s)
