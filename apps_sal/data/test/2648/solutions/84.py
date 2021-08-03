from collections import Counter

N = int(input())
a = list(map(int, input().split()))

na = len(set(a))
cnt = Counter(a)
ls = cnt.most_common()
lst = [2 for i in ls if i[1] % 2 == 0]

if len(lst) % 2 == 1:
    print((na - 1))
else:
    print(na)
