s = input()
k = int(input())
w = list(map(int, input().split()))
m = max(w)
sum = m * (2 * len(s) + k + 1) * k // 2
for i in range(len(s)):
    sum += w[ord(s[i]) - ord('a')] * (i + 1)
print(sum)
