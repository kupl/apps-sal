# sorry for the source code iam a newbie in Python
import collections
n = int(input())
s = []
for i in range(3):
    s.append(list(map(int,input().split())))
print(list(collections.Counter(s[0]) - collections.Counter(s[1]))[0])
print(list(collections.Counter(s[1]) - collections.Counter(s[2]))[0])


