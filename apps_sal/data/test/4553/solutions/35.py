a, b = map(int, input().split())
s = list(input())

if len(s) == a + b + 1:
    if s[a] == "-":
        del s[a]
        try:
            if all([0 <= int(x) <= 9 for x in s]):
                print("Yes")
            else:
                print("No")
        except:
            print("No")
    else:
        print("No")
else:
    print("No")
