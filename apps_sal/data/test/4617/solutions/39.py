c1 = str(input())
c2 = str(input())

if c2 == c1[::-1] and c1 == c2[::-1]:
    print("YES")
else:
    print("NO")
