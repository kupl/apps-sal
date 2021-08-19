s = input()
n = int(input())
for i in range(n):
    (l, r, k) = map(int, input().split())
    l -= 1
    r -= 1
    k %= len(s[l:r + 1])
    s = s[:l] + s[r - k + 1:r + 1] + s[l:r - k + 1] + s[r + 1:]
print(s)
