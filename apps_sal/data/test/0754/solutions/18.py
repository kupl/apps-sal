n = int(input())
line = input()
ans = 0
for i in range(1, len(line)):
    if line[i] == line[i - 1]:
        ans += 1
print(ans)

