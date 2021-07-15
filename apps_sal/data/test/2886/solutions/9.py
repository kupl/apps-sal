s = input()
for i in range(len(s)-1):
    if s[i:i+3].count(s[i]) >=2:
        print("{} {}".format(i+1, min(len(s), i+3)))
        break
else:
    print("-1 -1")
