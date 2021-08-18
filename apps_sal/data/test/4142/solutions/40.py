s = input()
s = list(s)
odd_list = s[0::2]
even_list = s[1::2]

if "R" not in even_list and "L" not in odd_list:
    print("Yes")
else:
    print("No")
