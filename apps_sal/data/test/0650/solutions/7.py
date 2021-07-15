s = str(input())
straight = ["A", "E", "F", "H", "I", "K", "L", "M", "N", "T", "V", "W","X", "Y", "Z"]
bendy = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if i not in straight]
ans=0
for i in s:
    if i in straight:
        ans+=1
if ans % len(s) == 0:
    print("YES")
else:
    print("NO")
