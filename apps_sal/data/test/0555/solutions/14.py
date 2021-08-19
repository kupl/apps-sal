a = input()
b = a[0]
ans = b if int(b) < 5 or int(b) == 9 else str(9 - int(b))
for i in a[1:]:
    j = int(i)
    if j > 4:
        ans += str(9 - j)
    else:
        ans += i
print(str(int(ans)))
