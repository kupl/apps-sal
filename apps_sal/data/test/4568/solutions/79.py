n = int(input())
a = input()
dic = 'abcdefghijklmnopqrstuvwxyz'
maxcount = 0
for i in range(n):
    count = 0
    for j in range(26):
        if str(dic[j]) in a[:i] and str(dic[j]) in a[i:]:
            count += 1
    maxcount = max(count, maxcount)
print(maxcount)
