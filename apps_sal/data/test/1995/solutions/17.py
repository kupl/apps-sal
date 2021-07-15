s = input()
for it in range(int(input())):
    l, r, k = list(map(int, input().split()))
    k %= r - l + 1
    s = s[:l - 1] + s[r - k: r] + s[l - 1: r - k] + s[r:]
print(s)

