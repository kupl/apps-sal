s = input()
m = int(input())
for it in range(m):
    l, r, k = [int(i) for i in input().split()]
    l -= 1
    k = k % (r - l)
    s = s[:l] + s[r - k: r] + s[l: r - k] + s[r:]
print(s)
