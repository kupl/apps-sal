def anagram(s):
    dic = {}
    for moji in s:
        dic.setdefault(moji, 0)
        dic[moji] += 1
    sort_list = sorted(dic)
    ans = ''
    for moji in sort_list:
        ans += moji + str(dic[moji])
    return ans


n = int(input())
s = []
ans_dic = {}
for i in range(n):
    s.append(anagram(str(input())))
    ans_dic.setdefault(s[i], 0)
    ans_dic[s[i]] += 1
ans = 0
for val in ans_dic.values():
    ans += val * (val - 1) // 2
print(ans)
