a = list(input())
count = 0
for i in range(0, len(a)):
    if a[i] == "9":
        count += 1

if count > 0:
    print("Yes")
else:
    print("No")
