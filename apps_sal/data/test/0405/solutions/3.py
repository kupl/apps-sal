n = int(input())
s = input()
cnt = 0
for i in s:
    if i != '<': break
    cnt += 1
for i in s[::-1]:
    if i != '>': break
    cnt += 1
print(cnt)

