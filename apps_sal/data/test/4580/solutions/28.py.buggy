with open(0) as f:
    N, *a = list(map(int, f.read().split()))
Set = set()
free = 0
for x in a:
    x //= 400
    if x < 8:
        Set.add(x)
    else:
        free += 1

Ans = [max(1, len(Set)), len(Set) + free]
print((*Ans))
