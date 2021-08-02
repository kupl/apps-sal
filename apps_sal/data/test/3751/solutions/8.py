s = input()

mx = ord('a')
flag = True

for c in s:
    if ord(c) > mx:
        print("NO")
        flag = False
        break
    if ord(c) == mx:
        mx = mx + 1

if flag:
    print("YES")
