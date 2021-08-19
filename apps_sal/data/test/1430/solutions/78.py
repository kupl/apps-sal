import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
(n, k) = list(map(int, input().split()))
s = input()
ans = 0
cnt = 0
right = 1
for left in range(0, n):
    if left == 0 and s[left] == '0':
        cnt += 1
    if left > 0 and s[left] == '1' and (s[left - 1] == '0'):
        cnt -= 1
    while right <= n - 1:
        if s[right] == '0' and s[right - 1] == '1':
            if cnt < k:
                cnt += 1
            else:
                break
        right += 1
    ans = max(ans, right - left)
print(ans)
