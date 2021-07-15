n = int(input())
s = list(input())
if n == 1:
    print("Yes")
    return
for i in range(n):
    if s.count(s[i]) > 1:
        print("Yes")
        return
print("No")
