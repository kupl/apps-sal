N = input()
is_lucky_7 = 0
for i in N:
    if i == "7":
        is_lucky_7 = True
        break
if is_lucky_7:
    print("Yes")
else:
    print("No")
