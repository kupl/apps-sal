n = int(input())
dic = {}
cnt = 0

for i in range(n):
    s = input()
    if s[0] == "M" or s[0] == "A" or s[0] == "R" or s[0] == "C" or s[0] == "H":
        if s[0] in dic:
            dic[s[0]] += 1
        else:
            dic[s[0]] = 1

lis = [x for x in dic.values()]

for j in range(len(lis) - 2):
    for k in range(j + 1, len(lis) - 1):
        for l in range(k + 1, len(lis)):

            cnt += lis[j] * lis[k] * lis[l]

print(cnt)
