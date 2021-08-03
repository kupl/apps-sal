n = int(input())
s = list(input())
if n % 2 == 0:
    bef = s[:n // 2]
    aft = s[n // 2:]
    if bef == aft:
        print("Yes")
    else:
        print("No")
else:
    print("No")
