n = int(input())
s = input()

flag = False

for i in range(len(s) - 1):
    if flag:
        break
    if s[i] != s[i + 1]:
        print("YES")
        print(s[i:i+2])
        flag = True
if not flag:
    print("NO")
