length = int(input())
num = 2*length-2
all_lst = []
longest = []
for i in range(num):
  string = input()
  all_lst.append(string)
  if(len(string) == length -1):
    longest.append(string)
cand_a = longest[0][0] + longest[1]
cand_b = longest[1][0] + longest[0]
cand_a_lst = []
for i in range(length-1):
  cand_a_lst.append(cand_a[:i+1])
  cand_a_lst.append(cand_a[i+1:])
ans = []
count = [0 for i in range(length-1)]
x, y = sorted(cand_a_lst), sorted(all_lst)
if(x == y):
  for mem in all_lst:
    if(mem == cand_a[:len(mem)] and count[len(mem)-1]==0):
      #print(mem + " " + cand_a[:len(mem)])
      ans.append("P")
      count[len(mem)-1] = 1
    else:
      #print(mem + " " + cand_a[length-len(mem):])
      ans.append("S")
else:
  for mem in all_lst:
    if(mem == cand_b[:len(mem)] and count[len(mem)-1]==0):
      #print(mem + " " + cand_a[:len(mem)])
      ans.append("P")
      count[len(mem)-1] = 1
    else:
      #print(mem + " " + cand_a[length-len(mem):])
      ans.append("S")
print("".join(ans))
