n = int(input())
A = map(int, input().split())
flag = True

for a in A:
  if a%2 != 0:
    continue
  if a%3 != 0 and a%5 != 0:
    flag = False
    break

print("APPROVED" if flag else "DENIED")
