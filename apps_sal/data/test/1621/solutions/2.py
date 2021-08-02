s = input()
k = int(input())
w = list(map(int, input().split()))

res = 0
max_w = max(w)
for i in range(len(s) + k):
    if i < len(s):
        res += (i + 1) * w[ord(s[i]) - ord('a')]
    else:
        res += (i + 1) * max_w
print(res)
