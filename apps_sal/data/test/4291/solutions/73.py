(n, q) = map(int, input().split())
s = list(input())
num = [0] * n
count = 0
for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        count += 1
    num[i + 1] = count
for i in range(q):
    (l, r) = map(int, input().split())
    ans = num[r - 1] - num[l - 1]
    print(ans)
