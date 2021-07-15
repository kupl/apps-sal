k = int(input())
a = [int(i) for i in input().split()]
an = max(a) - 25
if an <= 0:
    print(0)
else:
    print(an)

