s = str(input())


for i in range(2, len(s), 2):
    line = s[:len(s) - i]
    if line[:len(line) // 2] == line[len(line) // 2:]:
        ans = len(line)
        break


print(ans)
