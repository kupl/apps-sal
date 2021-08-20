n = int(input())
s = set()
l = list(map(int, input().split()))
cnt = 0
for x in l:
    if x in s:
        s.remove(x)
    else:
        s.add(x)
    cnt = max(cnt, len(s))
print(cnt)
