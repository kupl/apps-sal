s=input()
rem=3 if s[0]==s[-1] else 2
if (len(s)-rem)%2==0:
    print("Second")
else:
    print("First")

