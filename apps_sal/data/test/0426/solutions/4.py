import sys
#
# a, b, c, d = sorted(list(map(int, input().split())))
# if a + b == c + d or a + c == b + d or a + d == b + c:
#     print("YES")
# else:
#     print("NO")
n, k = map(int, input().split())
s = input()
if len(s) == 1 and k > 0:
    print(0)
    return
if s[0] != "1":
    if k > 0:
        k -= 1
        print("1", end="")
    else:
        print(s[0], end="")
else:
    print("1", end="")
for i in s[1:]:
    if i == "0":
        print(0, end="")
    else:
        if k > 0:
            k -= 1
            print(0, end="")
        else:
            print(i, end="")
