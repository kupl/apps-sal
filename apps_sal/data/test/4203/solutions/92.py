#104B
s = input()
c_list = []
c_count = 0
answer = "WA"
for i in range(2,len(s)-1):
    if s[i] == "C":
        c_list.append(i)
    if s[i].islower() == False:
        c_count += 1
if s[0]=="A" and s[1].islower()==True and s[-1].islower()==True and len(c_list)==1 and c_count==1:
    answer="AC"
print(answer)
