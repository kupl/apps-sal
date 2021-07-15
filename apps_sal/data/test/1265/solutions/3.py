import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

if len(first) != len(second):
    print("NO")
    return

count1, count2 = 0, 0
for i in first:
    if i == '1':
        count1 += 1
for i in second:
    if i == '1':
        count2 += 1

if (count1 == 0 and count2 != 0) or \
  (count1 != 0 and count2 == 0):
  print("NO")
  return

print("YES")

