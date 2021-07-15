def count(list):
    dict = {}
    for i in range(len(list)):
        dict[list[i]] = dict.get(list[i], 0) + 1
    return dict

n = int(input())
a = list(map(int,input().split()))
dic = count(a)
ans = 0

for i, x in dic.items():
    differ = x - i
    if differ>0:
        ans += differ
    elif differ<0:
        ans += x

print(ans)
