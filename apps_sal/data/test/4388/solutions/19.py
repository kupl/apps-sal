s = input()
s_list=list(s)
for i in range(len(s)):
  if s[i] == "1":
    s_list[i]='9'
  elif s[i]=="9":
    s_list[i]='1'
str_changed="".join(s_list)
print(str_changed)

