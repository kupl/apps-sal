n = int(input())
line = input()
check = False
for i in range(1, (n // 4) + 1):
    for j in range((n - i * 4)):
        if line[j] == "*":
            if line[j] == line[j + i] == line[j + 2 * i] == line[j + 3 * i] == line[j + 4 * i]:
                print("yes")
                check = True
                break
    if check:
        break
if not check:
    print("no")
