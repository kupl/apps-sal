c = [list(input())for i in range(2)]
if c[0][0] == c[1][2] and c[0][1] == c[1][1] and c[0][2] == c[1][0]:
    print("YES")
else:
    print("NO")
