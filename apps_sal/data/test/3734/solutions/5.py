days = "monday tuesday wednesday thursday friday saturday sunday".split()

offs = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d1 = days.index(input())
d2 = days.index(input())

for o in offs:
    if (d1 + o) % 7 == d2:
        print("YES")
        break
else:
    print("NO")
