from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a = Counter(a).most_common()
num = 0
for (i, j) in a:
    if i < j:
        num += j - i
    elif j < i:
        num += j
print(num)
