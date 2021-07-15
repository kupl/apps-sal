s = str(input())
ss = [int(i) for i in s]
k = int(input())
if sum(ss) == len(s):
  print("1")
  return
count = 0
while s[count] == "1":
  if k == count + 1:
    print("1")
    return
  count += 1
print(s[count])
