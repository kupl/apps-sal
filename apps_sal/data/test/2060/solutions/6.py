n = int(input())

for i in range(n):
    x = int(input())
    possible = False
    for s in range(x // 3 + 2):
        for l in range(x // 7 + 2):
            if s * 3 + l * 7 == x:
                possible = True
    print("YES" if possible else "NO")
