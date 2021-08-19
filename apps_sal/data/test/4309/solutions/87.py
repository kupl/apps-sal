n = input()
if int(n[1]) < int(n[0]):
    ans = int(n[0] * 3)
elif int(n[0]) == int(n[1]) and int(n[2]) <= int(n[1]):
    ans = int(n[0] * 3)
else:
    ans = int(str(int(n[0]) + 1) * 3)
print(ans)
