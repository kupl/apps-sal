s = input()
n = int(input())
for i in range(n):
    (l, r, k) = map(int, input().split())
    k %= r - l + 1
    seg = s[l - 1:r]
    seg = seg[len(seg) - k:] + seg[:len(seg) - k]
    s = s[:l - 1] + seg + s[r:]
print(s)
