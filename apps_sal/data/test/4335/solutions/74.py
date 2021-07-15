n = int(input())
s = input()
if n%2 == 0:
  if s[:n//2] == s[n//2:]:
    print("Yes")
    return
print("No")
