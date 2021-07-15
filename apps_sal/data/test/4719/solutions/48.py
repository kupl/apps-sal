n = int(input())
jisho = 'abcdefghijklmnopqrstuvwxyz'
moji = []
#print(moji)
for i in range(n):
    dic = {}
    for i in range(len(jisho)):
        dic.setdefault(jisho[i],0)
    s = str(input())
    for j in range(len(s)):
        dic.setdefault(s[j],0)
        dic[s[j]] += 1
    moji.append(dic)
dic = {}
for j in range(len(jisho)):
    tmp = 50
    for i in range(n):
        tmp = min(tmp,moji[i][jisho[j]])
    if tmp != 0:
        dic.setdefault(jisho[j],tmp)
#print(dic)
ans = ''
for item in dic.items():
    while dic[item[0]]>0:
        ans += item[0]
        dic[item[0]] -= 1
print(ans)
