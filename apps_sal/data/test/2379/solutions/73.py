n, k, c = list(map(int, input().split()))
s = input()
left = [k + 1] * n
right = [k + 1] * n
l, r = 1, 1
i = 0
while i < n:
    if s[i] == 'o':
        left[i] = l
        l += 1
        i += c
    i += 1
i = 1
while i < n + 1:
    if s[-i] == 'o':
        right[-i] = r
        r += 1
        i += c
    i += 1
for i in range(n):
    if left[i] + right[i] == k + 1:
        print((i + 1))
