# cook your dish here
testCases=int(input())
answers=[]
for i in range (testCases):
    a=input().split()
    answers.append(a)
count = 0
for i in range(testCases):
    flag = 0
    ans=answers[i].count('T')
    #print(answers[i])
    for j in range (testCases):
     if answers[i][j] =='T' and i!=j :
      if answers[i] == answers [j]:
       continue
      else:
  #           print("HII")
       flag=1
       break
    if flag==0 and count<ans:
     count=ans
print(count)
