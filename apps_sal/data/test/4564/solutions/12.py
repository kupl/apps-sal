S=input()
for c in S:
    if S.count(c)>1:
        print("no")
        break
else:
    print("yes")

