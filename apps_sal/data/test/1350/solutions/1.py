read = lambda: map(int, input().split())
n, k = read()
s = input()
c = [0] * 26
for i in range(n):
    if s[i] <= chr(ord('A') + k - 1):
        c[ord(s[i]) - ord('A')] += 1
print(min(c[:k]) * k)
