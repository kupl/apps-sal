n, k, c = list(map(int, input().split()))
s = input()
l = [0] * n
pre = n + c + 1
cnt = k
for i in range(n - 1, -1, -1):
    if s[i] == "o" and -(i) + pre > c and cnt > 0:
        pre = i
        l[i] = cnt
        cnt -= 1
pre = -c - 5
cnt = 0
for i in range(n):
    if s[i] == "o" and i - pre > c and cnt < k:
        pre = i
        cnt += 1
        if l[i] == cnt:
            print((i + 1))
