n = int(input())
s = list(map(str, input().split()))
s = set(s)

if len(s) == 3:
    print("Three")
else:
    print("Four")
