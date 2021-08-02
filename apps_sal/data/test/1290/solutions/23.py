s = input().split()
n = int(s[0])
m = int(s[1])
s = list(map(int, input().split()))
dic = {}
for i in range(n):
    dic.update({i + 1: 0})
for x in s:
    dic[x] += 1

mn = 10**9
for x in dic.keys():
    if dic[x] < mn:
        mn = dic[x]

print(mn)
