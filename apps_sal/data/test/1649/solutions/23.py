

delic = list(map(int, input().split()))
delic.sort()

if delic[0] + delic[3] == delic[1] + delic[2]:
    print("Yes")
elif sum(delic[0:3]) == delic[3]:
    print("Yes")
else:
    print("No")
