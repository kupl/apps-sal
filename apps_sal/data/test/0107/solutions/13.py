a = input()

n = len(a)

for i in range(n):
    if a[i] == '1':
        tot = 0
        for j in range(i + 1, n):
            if a[j] == '0':
                tot += 1
                if tot == 6:
                    print("yes")
                    return

print("no")
