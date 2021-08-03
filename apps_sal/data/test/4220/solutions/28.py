num = int(input())
line = input()
lines = list(line)
if len(lines) <= num:
    print(line)
else:
    for i in range(num):
        print(lines[i], end="")
    print("...")
