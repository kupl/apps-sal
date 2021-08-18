n = int(input())
ss = set()
l = input().split()
for s in l:
    ss.add(''.join(sorted(str(set(s)))))
print(len(ss))
