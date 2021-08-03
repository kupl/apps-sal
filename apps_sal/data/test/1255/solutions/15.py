from collections import Counter
a = int(input())
sa = []
string = ''
bad = []
for x in range(a):
    string = ''
    sa = input().split(' ')
    string += sa[0]
    string += '+'
    string += sa[1]
    bad.append(string)
a = Counter(bad).most_common(1)
print(a[0][1])
