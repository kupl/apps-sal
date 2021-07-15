n = int(input())

dd = {}

for _ in range(n):
    l = input()
    if l in dd:
        print("YES")
    else:
        print("NO")
    dd[l] = 1


