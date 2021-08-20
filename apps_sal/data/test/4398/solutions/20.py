n = int(input())
(s, t) = input().split()
li = []
for i in range(n):
    li.append(s[i] + t[i])
stra = ''.join(li)
print(stra)
