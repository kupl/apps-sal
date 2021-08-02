n, m = map(int, input().split())
s = list(map(int, input().split()))
t = 0
k = 0
for i in range(len(s)):
    k = (t + s[i]) // m
    print(k, end=" ")
    t = (t + s[i]) % m
