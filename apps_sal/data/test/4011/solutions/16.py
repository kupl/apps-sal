n = int(input())
s = [int(item) for item in list(input())]
f = [0] + [int(item) for item in input().split()]

new_s = [0] * n
for i in range(n):
    new_s[i] = f[int(s[i])]

i = 0
idx = -1
for j in range(n):
    if new_s[j] > s[j]:
        idx = j
        break

if idx == -1:
    print(''.join(str(item) for item in s))
else:
    start = idx
    while idx < n and new_s[idx] >= s[idx]:
        idx += 1
    u = [str(item) for item in s[:start]]
    v = [str(item) for item in new_s[start:idx]]
    w = [str(item) for item in s[idx:]]
    assert(len(u) + len(v) + len(w) == n)
    print(''.join(u) + ''.join(v) + ''.join(w))
