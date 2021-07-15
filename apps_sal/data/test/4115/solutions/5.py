s = input()
length = len(s)//2
count = 0
for i in range(length):
  if s[i] != s[-(i+1)]:
    count += 1
print(count)
