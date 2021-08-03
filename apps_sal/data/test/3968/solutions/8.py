a = int(input())
b = list(map(int, input().split(" ")))
if b.count(1) >= 1 and b.count(2) >= 1:
    b.remove(1)
    b.remove(2)
    b.sort(reverse=True)
    b.insert(0, 2)
    b.insert(1, 1)
    print(*b, sep=" ")
else:
    print(*b, sep=" ")
