n=input()
if len(set(n[:3]))==1 or len(set(n[1:4]))==1:
    print("Yes")
else:
    print("No")
