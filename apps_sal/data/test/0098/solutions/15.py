a1, b1 = list(map(int, input().split()))
a2, b2 = list(map(int, input().split()))
a3, b3 = list(map(int, input().split()))

if a2+b3<=b1:
    if max(a3,b2)<=a1:
        print("YES")
        return
if a2+b3<=a1:
    if max(a3,b2)<=b1:
        print("YES")
        return

if a2+a3<=b1:
    if max(b2,b3)<=a1:
        print("YES")
        return
if a2+a3<=a1:
    if max(b2,b3)<=b1:
        print("YES")
        return
if b2+a3<=a1:
    if max(a2,b3)<=b1:
        print("YES")
        return
if b2+a3<=b1:
    if max(a2,b3)<=a1:
        print("YES")
        return
if b2+b3<=a1:
    if max(a2,a3)<=b1:
        print("YES")
        return
if b2+b3<=b1:
    if max(a2,a3)<=a1:
        print("YES")
        return
print("NO")

