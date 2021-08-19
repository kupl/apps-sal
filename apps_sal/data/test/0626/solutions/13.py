n = int(input())
a = [int(x) for x in input().split()]
k = 0
t = -1
while a:
    t += 1
    next_a = []
    for elem in a:
        if elem <= k:
            k += 1
        else:
            next_a.append(elem)
    next_a.reverse()
    a = next_a
print(t)
