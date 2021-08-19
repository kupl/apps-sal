s = input()
if s[0] == s[len(s) - 1]:
    # a bab a
    if len(s) % 2 == 0:
        print("First")
    else:
        print("Second")
else:
    # a baba b
    if len(s) % 2 == 1:
        print("First")
    else:
        print("Second")
