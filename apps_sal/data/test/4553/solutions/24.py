a, b = list(map(int, input().split()))
s = input()
ans = True
for i in range(a + b + 1):
    if s[a] != "-":
        ans = False
        break
    else:
        if i == a:
            pass
        else:
            for j in range(10):
                if s[i] == str(j):
                    break
            else:
                ans = False

if ans:
    print("Yes")
else:
    print("No")
