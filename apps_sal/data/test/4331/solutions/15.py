N = input()
ans = 0
for i in range(len(N)):
    if N[i] == '7':
        ans = 1
        break
if ans == 1:
    print("Yes")
else:
    print("No")
