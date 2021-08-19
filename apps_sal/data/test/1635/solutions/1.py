n = int(input())
data = list(map(int, input().split()))
was = {}
for i in range(n):
    was[data[i]] = i
print(min(list(was.keys()), key=was.get))
