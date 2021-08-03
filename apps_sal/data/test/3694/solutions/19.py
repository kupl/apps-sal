from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
c = Counter(arr)
common = c.most_common(2)
if common[0][1] > 2 \
        or (common[0][1] == 2 and (common[0][0] == 0 or (common[0][0] - 1) in c)) \
        or (len(common) == 2 and common[1][1] == 2):
    print('cslnb')
else:
    if (sum(arr) - (n * (n - 1)) // 2) % 2 == 1:
        print('sjfnb')
    else:
        print('cslnb')
