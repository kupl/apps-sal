n = int(input())
a = list(map(int,input().split()))
q = 0
c = 0
while len(a) > 0:
    de = set()
    for i in range(len(a)):
        if a[i] <= q:
            q += 1
            de.add(i)
    c += 1
    a = [a[i] for i in reversed(range(len(a))) if i not in de]
print(c-1)
