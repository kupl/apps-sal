sa = int(input())
sa2 = input().split(' ')
sa3 = [int(x) for x in sa2]
sumx = sum(sa3)
t = 0
for sa4 in range(1, 6):
    if (sumx + sa4) % (sa + 1) != 1:
        t += 1
print(t)
