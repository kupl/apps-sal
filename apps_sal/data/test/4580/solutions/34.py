def cordtest(AAA):
  jisyo ={'H':0,'C':0,'G':0,'M':0,'B':0,'Y':0,'O':0,'R':0,'A':0}
  for i in AAA:
    
    if i <= 399:
      jisyo['H'] +=1
    elif 400 <= i <=799:
      jisyo['C'] +=1
    elif 800 <= i <=1199:
      jisyo['G'] +=1
    elif 1200 <= i <=1599:
      jisyo['M'] +=1
    elif 1600 <= i <=1999:
      jisyo['B'] +=1
    elif 2000 <= i <=2399:
      jisyo['Y'] +=1
    elif 2400 <= i <= 2799:
      jisyo['O'] +=1
    elif 2800 <= i <= 3199:
      jisyo['R'] +=1
    else:
      jisyo['A'] +=1
  maxi = 0
  mini = 0
  for i,j in jisyo.items():
    
    if i != 'A':
      if j >0:
        mini +=	1
    else:
      maxi += j
  ans = maxi + mini
  if mini ==0:
    mini =1
  
  return print(mini,ans)
N = int(input())
AA = list(map(int,input().split()))
cordtest(AA)
      
      
  
