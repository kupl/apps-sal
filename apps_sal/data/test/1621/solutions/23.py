s, k, w = input(), int(input()), list(map(int, input().split()))

sum, m, l = 0, max(w), len(s)
for i in range(l + k):
    sum += (w[ord(s[i]) - ord('a')] if i < l else m) * (i + 1)

print(sum)

