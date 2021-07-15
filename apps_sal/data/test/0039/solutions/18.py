s = input()
if (s!=s[::-1]):
    print(len(s))
else:
    if (len(set(s))==1):
        print(0)
    else:
         print(len(s)-1)

