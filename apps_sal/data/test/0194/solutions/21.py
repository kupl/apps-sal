n, one, two = map(int, input().split())
arr = list(map(int, input().split()))

two_one = 0
fail = 0

for x in arr[:n]:
    if x == 1:
        if one > 0:
            one -= 1
        elif two > 0:
            two -= 1
            two_one += 1
        elif two_one > 0:
            two_one -= 1
        else:
            fail += 1
    else:
        if two > 0:
            two -= 1
        else:
            fail += 2

print(fail)
