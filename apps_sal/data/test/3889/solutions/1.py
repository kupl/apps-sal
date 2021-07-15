n = input()
s=  input()


if len(s) == 1:
    print("Yes")
else:
    if len(s) == len(set(s)):
        print("No")
    else:
        print("Yes")
