testcases = int(input())
count = 0
bool = False
for i in range(testcases):
    a = input()
    if a[0] == a[-1]:
        count += 1
        if count == 3:
            print("Yes")
            bool = True
            break
    else:
        count = 0
if not bool:
    print("No")
