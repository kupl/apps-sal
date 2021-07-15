from collections import Counter
n = int(input())
s = []
for i in range(n):
    s1 = ''.join(sorted(input()))
    s.append(s1)
s = Counter(s).most_common()
num = 0
for i,h in s:
    num += (h*(h-1))//2
print(num)
