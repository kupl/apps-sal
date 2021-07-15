s=input();
alph=[0 for x in range (0,26)];
for i in s:
	alph[ord(i)-ord('a')]=alph[ord(i)-ord('a')]+1;
for i in range (25,-1,-1):
	if (alph[i]%2!=0):
		for j in range (0,26):
			if (alph[j]%2!=0):
				alph[i]=alph[i]-1;
				alph[j]=alph[j]+1;
				break;
r="";
for i in range (0,26):
	while(alph[i]>1):
		r=r+chr(ord('a')+i);
		alph[i]=alph[i]-2;
s=r;
for i in range (0,26):
	if (alph[i]!=0):
		r=r+chr(ord('a')+i);
		
print((r+s[::-1]));

