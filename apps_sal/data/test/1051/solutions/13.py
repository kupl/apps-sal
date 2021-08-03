k = input()
arr = input()

max = 0

for item in arr.split():
    if int(item) > max:
        max = int(item)

if (max - 25 > 0):
    print(max - 25)
else:
    print(0)
