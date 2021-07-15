n = int(input())
a = list(map(int, input().split()))
s = set()
for i in a:
    j = i
    while j in s:
        s.remove(j)
        j += 1
    s.add(j)
print(max(s)-len(s)+1)

