s = input()

count = 0
for i in range(len(s)):
    if i % 2 == 0 and s[i] == "L":
        count += 1
    if i % 2 == 1 and s[i] == "R":
        count += 1

if count > 0:
    print("No")
else:
    print("Yes")
