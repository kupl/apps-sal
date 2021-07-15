n = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))
o = set()
i = 0
j = 0
while j < n:
    if d[i] in o:
        i += 1
    elif d[i] != p[j]:
        o.add(p[j])
        j += 1
    else:
        i += 1
        j += 1
print(len(o))
