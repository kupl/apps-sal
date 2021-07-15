s=input(str())
lst=["eraser","erase","dreamer","dream"]
for t in lst:
    s=s.replace(t,"")
if s=="":
    print("YES")
else:
    print("NO")

