from collections import Counter
s = input()
count = Counter(s)
c0 = count['0']
c1 = count['1']
print(min(c0, c1) * 2)
