import re
a = input()
a = input()
org = a
inclam = re.findall('\\(.*?\\)', a)
for i in inclam:
    a = a.replace(i, '_')
words = a.split('_')
c = max(list(map(len, words)))
count = 0
for i in inclam:
    count += len(list([_f for _f in i.replace('(', '_').replace(')', '_').split('_') if _f]))
print(c, count)
