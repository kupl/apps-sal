n = int(input())
a = [int(x) for x in input().split()]
one = a.count(1)
two = a.count(2)
if one == two:
    print(one)
elif two > one:
    print(one)
else:
    ans = two
    ans = ans + int((one - two) / 3)
    print(ans)
