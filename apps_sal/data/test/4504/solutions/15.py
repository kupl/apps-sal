s = str(input())


# print(kind)
for i in range(2, len(s), 2):
    line = s[:len(s) - i]
    # print(line)
    if line[:len(line) // 2] == line[len(line) // 2:]:
        ans = len(line)
        break


print(ans)
