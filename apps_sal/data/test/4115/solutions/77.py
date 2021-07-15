S = input()
s1 = S[:len(S)//2]
s2 = S[len(S)//2+len(S)%2:]
s2 = s2[::-1]
count = 0
for i in range(len(s1)):
  if s1[i] != s2[i]:
    count += 1
print(count)
