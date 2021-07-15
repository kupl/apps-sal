n = int(input())
w = input()
s = set([w])
l = w[-1]
for i in range(n-1):
    w = input()
    if w not in s:
        s.add(w)
        if w[0] != l:
            print("No")
            break
        else:
            l = w[-1]
    else:
        print("No")
        break
else:
    print("Yes")
