str1 = input()
str2 = input()

count = 0
for i in range(len(str1)):
  if(str1[i] != str2[i]):
    count+=1
    
print(count)
