from collections import defaultdict
import sys
s = input()
n = len(s)
dic = defaultdict(int)

for i in range(n):
    dic[s[i]] += 1
    if dic[s[i]]==2:
        print("no")
        return

print('yes')
