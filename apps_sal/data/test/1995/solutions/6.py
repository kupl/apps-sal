s = input()
m = int(input())
for i in range(m):
    (l, r, k) = [int(x) for x in input().split()]
    start = s[:l - 1]
    middle = s[l - 1:r]
    end = s[r:]
    ln = r - l + 1
    k %= ln
    middle_e = middle[:ln - k]
    middle_s = middle[ln - k:]
    s = start + middle_s + middle_e + end
print(s)
