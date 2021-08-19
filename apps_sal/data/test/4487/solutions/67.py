a, b, c = input().split()
# しりとりが成り立っているかを確認
if a[-1] == b[0] and b[-1] == c[0]:
    print("YES")
else:
    print("NO")
