s = input()
n = int(input())
(a, b) = ([0 for i in range(n)], [0 for i in range(n)])
for i in range(0, n):
    (a[i], b[i]) = list(map(int, input().split()))
count = [0 for i in range(len(s))]
count[0] = 0
for i in range(1, len(s)):
    count[i] = count[i - 1]
    if s[i - 1] == s[i]:
        count[i] += 1
for i in range(0, n):
    print(count[b[i] - 1] - count[a[i] - 1])
