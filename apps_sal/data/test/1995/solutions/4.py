s = input()
n = int(input())
for i in range(n):
    (l, r, k) = map(int, input().split())
    ds = k % (r - l + 1)
    s = s[:l - 1] + s[r - ds:r] + s[l - 1:r - ds] + s[r:]
print(s)
