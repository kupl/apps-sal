n = int(input())
s = list(input())
if n % 2 == 1:
    print("No")
    return

s = [0 if x == "(" else 1 for x in s]
if sum(s) != n // 2:
    print("No")
    return

count = 0
for i in range(n):
    if s[i] == 0:
        count += 1
    else:
        count -= 1
    if count <= -2:
        print("No")
        return
print("Yes")

