n = int(input())
s = input()
if len(set(list(s))) == 1:
    print("NO")
else:
    print("YES")
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            print(s[i] + s[i + 1])
            break
