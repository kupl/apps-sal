s = input()
x = (len(s) // 2) + 1
z = 0
for i in range(x):
    a = s[0:(x + i)]
    if s.startswith(a) and s.endswith(a) and len(a) < len(s):
        print('YES')
        print(a)
        z += 1
        break
    else:
        pass
if z == 0:
    print("NO")
