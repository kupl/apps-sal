s = input()

l = len(s) // 2
o = 0
if len(s) % 2 != 0:
    o = 1
for i in range(1, l):
    # print(i)
    # print(s[:i+l], s[l-i:])
    if s[:l + i] == s[o + l - i:]:
        print("YES")
        print(s[:i + l])
        break
else:
    print("NO")
