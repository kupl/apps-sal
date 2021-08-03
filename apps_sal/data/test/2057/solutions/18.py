n = int(input())
m = list(map(int, input().split(' ')))
s = set()
s.add(1)
for i in range(1, len(m)):
    try:
        s.remove(m[i])
        s.add(i + 1)
    except:
        s.add(i + 1)
print(len(s))
