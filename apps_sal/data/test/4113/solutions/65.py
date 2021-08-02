n = int(input())
s = "No"

for i in range(n):
    for j in range(n):
        if 4 * i + 7 * j == n:
            s = "Yes"
            break

print(s)
