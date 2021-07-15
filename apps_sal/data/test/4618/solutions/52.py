s = input()
k = int(input())

subs_list = []
for i in range(len(s)):
    for j in range(i+1, i+k+1):
        subs_list.append(s[i:j])

ans = sorted(set(subs_list))
print((ans[k-1]))

