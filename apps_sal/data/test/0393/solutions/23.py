n = int(input())
s = '0' + input() + '0'

if s == "00":
    print("No")

else:
    if "000" in s or "11" in s:
        print("No")
    else:
        print("Yes")
