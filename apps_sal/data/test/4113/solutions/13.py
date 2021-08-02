N = int(input())

check = False
for i in range(26):
    for j in range(15):
        if N == 4 * i + 7 * j:
            check = True

print("Yes" if check else "No")
