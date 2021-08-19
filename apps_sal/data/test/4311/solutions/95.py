a = int(input())
s = set([a])

for i in range(10**6):
    if a % 2 == 0:
        # print("Process for even.")
        a = a // 2
    else:
        # print("Process for odd.")
        a = 3 * a + 1
    if a not in s:
        s.add(a)
    else:
        print((i + 2))
        break
