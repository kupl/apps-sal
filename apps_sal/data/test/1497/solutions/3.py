a = int(input())
s = dict()
for i in range(a):
    cur = input()
    if s.get(cur) != None:
        s[cur] += 1
    else:
        s[cur] = 1
print(max(s.values()))
