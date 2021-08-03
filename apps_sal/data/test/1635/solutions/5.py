q = int(input())
a = list(map(int, input().split()))
s = {}
for i in range(0, q):
    s[a[i]] = i
d = min(s.values())
for i in s:
    if s[i] == d:
        print(i)
