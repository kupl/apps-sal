S = input()
S = S.replace("eraser","@").replace("erase","@").replace("dreamer","@").replace("dream","@")
if set(S) == set("@"):
    print("YES")
else:
    print("NO")
