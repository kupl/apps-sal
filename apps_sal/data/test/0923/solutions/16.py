n = input();
li = input();
n = int(n)
li = li.split()
valid = "Yes"
for i in range(0, n - 1):
    if (int(li[i]) + int(li[i + 1]) - 2 * i - 1) % n:
        valid = "No"
        break
print(valid)

