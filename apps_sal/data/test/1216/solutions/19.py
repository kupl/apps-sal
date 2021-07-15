n = int(input());
a = {'a', 'o', 'e', 'u','i','y'};
s = input();
curVolve = 'a';
curCount = 0;
ans = [];
i=0;
flag=0;
curRepeat = 'e';
while i<n:
  if s[i] in a:
    curVolve = s[i];
    if curVolve=='e' or curVolve=='o':
      if flag==2:
        if curRepeat==curVolve:
          ans.pop();
          while i<n  and s[i]==curVolve:
           i+=1;
          i-=1;
          flag=0;
        else:
          flag=1;
          curRepeat=curVolve;
          ans.append(s[i]);
      else:
        if flag==0:
          curRepeat=curVolve;
          flag=1;
          ans.append(s[i]);
        else:
          if curRepeat==curVolve:
            ans.append(s[i]);
            flag=2;
          else:
            curRepeat=curVolve;
            ans.append(s[i]);
            flag=1;
    else:
      flag=0;
      ans.append(s[i]);
      while i<n  and s[i]==curVolve :
        i+=1;
      i-=1;
  else:
    flag=0;
    ans.append(s[i]);
  i+=1;
  
print(''.join(ans))
