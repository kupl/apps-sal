N = int(input())
S = input()

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Sn = ""
for i in range(len(S)):
  Sn += abc[(abc.find(S[i])+N) % 26]
print(Sn)
