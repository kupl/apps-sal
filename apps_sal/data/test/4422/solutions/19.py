n,k = [int(x) for x in input().split()]
s = input()
 
k -= 1
s = list(s)

if s[k] == "A":
  s[k] = "a"
elif s[k] == "B":
  s[k] = "b"
elif s[k] == "C":
  s[k] = "c"
 
print("".join(s))
