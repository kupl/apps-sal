from collections import defaultdict
dic = defaultdict(int)
for i in range(int(input())):
    (a, b) = list(map(int, input().split()))
    dic[60 * a + b] += 1
print(max(dic.values()))
