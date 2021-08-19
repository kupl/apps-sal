n = int(input())
s = list(map(int, input().split()))
oddd = 0
evend = 0
for i in range(n):
    if s[i] % 2 == 0:
        oddd += 1
    else:
        evend += 1
if evend == 0:
    print(0)
elif oddd == 0:
    print(evend // 3)
elif oddd < evend:
    print(oddd + (evend - oddd) // 3)
else:
    print(evend)
