(n, q) = map(int, input().split())
s = input()
count = [0] * (n + 1)
for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        count[i + 1] = count[i] + 1
    else:
        count[i + 1] = count[i]
for i in range(q):
    (l, r) = map(int, input().split())
    print(count[r - 1] - count[l - 1])
