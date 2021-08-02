temp = input()
temp = input().split()
arr = [int(k) for k in temp]

s = sorted(list(set(arr)))

if len(s) > 3:
    print("NO")
elif len(s) < 3:
    print("YES")
else:
    if s[2] + s[0] == 2 * s[1]:
        print("YES")
    else:
        print("NO")
