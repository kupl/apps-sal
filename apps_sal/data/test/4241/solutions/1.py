def resolve(): 
   S = input();T=input()
   count1=[]
   for i in range(len(S)-len(T)+1):
       count2=0
       for j in range(len(T)):
           if S[i:i+len(T)][j]==T[j]:count2+=1
       count1.append(len(T)-count2)

   print(min(count1))
resolve()
