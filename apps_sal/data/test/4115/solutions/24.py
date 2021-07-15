s = input()

count = 0
for x in range(len(s)//2):
  if s[x] != s[-x-1]:
    count += 1

print(count)
