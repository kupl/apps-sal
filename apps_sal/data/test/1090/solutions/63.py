import copy

n, k = list(map(int, input().split()))
s = ['R'] + list(input()) + ['L']

cnt = 0
for i in range(1, n + 1):
    if s[i] == 'L' and s[i - 1] == 'L':
        cnt += 1
    if s[i] == 'R' and s[i + 1] == 'R':
        cnt += 1
# print(cnt)
while k > 0 and cnt < n - 1:
    if n - 1 - cnt > 1:
        cnt += 2
    elif n - 1 - cnt > 0:
        cnt += 1
    k -= 1
print(cnt)
