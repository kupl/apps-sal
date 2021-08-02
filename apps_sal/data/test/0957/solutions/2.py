s = input()
to_find = "heidi"
n = 0
for i in list(s):
    if i == to_find[n]:
        n += 1
    if n == 5:
        print("YES")
        break
else:
    print("NO")
