n = int(input())
for i in range(26):
    for j in range(15):
        if i * 4 + j * 7 == n:
            print("Yes")
            return
print("No")
