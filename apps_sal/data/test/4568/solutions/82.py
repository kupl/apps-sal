n = int(input())
s = input()
a = []
for i in range(1, n):
    a.append(len(set(s[:i]) & set(s[i:])))
print(max(a))
