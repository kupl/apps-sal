n = int(input())
s = input()
a = [0] * 300
for i in s:
    a[ord(i)] += 1
print((a.count(max(a)) ** len(s)) % (10**9 + 7))
