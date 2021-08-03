from collections import Counter
n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
dic = dict()
for k, v in cnt.items():
    dic[k] = v * (v - 1) // 2
res = sum(dic.values())
for ai in a:
    print(res - dic[ai] + int(dic[ai] * (cnt[ai] - 2) / cnt[ai]))
