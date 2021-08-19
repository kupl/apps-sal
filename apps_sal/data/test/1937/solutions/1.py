n = int(input())
b = list(map(int, input().split()))
a1 = [0]
a2 = [b[0]]
for x in b[1:]:
    new_a = a1[-1]
    if x - new_a > a2[-1]:
        new_a = x - a2[-1]
    new_a2 = x - new_a
    a1.append(new_a)
    a2.append(new_a2)
print(*a1 + a2[::-1])
