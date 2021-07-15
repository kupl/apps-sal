d = set([])
for i in range(1002):
    s = i*i
    d.add(s)

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
for i in a:
    if i not in d:
        print(i)
        break


