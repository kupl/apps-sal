n, m = [int(i) for i in input().split()]

photo = "#Black&White"

for i in range(n):
    s = input()
    if "C" in s or "M" in s or "Y" in s:
        photo = "#Color"
        break

print(photo)

