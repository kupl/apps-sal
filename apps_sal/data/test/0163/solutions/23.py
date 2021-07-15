n, k = list(map(int, input().split()))

line = input()

for x in range(n):
    if line[x] == "G":
        g = x    
    elif line[x] == "T":
        t = x

if (g - t) % k == 0:
    if g > t:
        while g > t:
            if g - k == t:
                print("YES")
                return
            elif line[g - k] == "#":
                print("NO")
                return
            else:
                g = g - k
    else:
        while g < t:
            if g + k == t:
                print("YES")
                return
            elif line[g + k] == "#":
                print("NO")
                return
            else:
                g = g + k
else:
    print("NO")
    return

