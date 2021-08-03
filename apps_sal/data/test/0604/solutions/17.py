n = int(input())
a = list(map(int, input().split()))
s = set()
for i in a:
    if not(i == 0):
        s.add(i)
print(len(s))
