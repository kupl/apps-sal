a = int(input())

for i in range(0, 10):
    if (a - i) % 10 == 0:
        ans = i

if ans == 3:
    print("bon")
elif ans == 0 or ans == 1 or ans == 6 or ans == 8:
    print("pon")
elif ans == 2 or ans == 4 or ans == 5 or ans == 7 or ans == 9:
    print("hon")
