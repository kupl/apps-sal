S=input()
S2=S[:(len(S)-1)//2]
S3=S[(len(S)+3)//2-1:]
if S==S[::-1] and S2==S2[::-1] and S3==S3[::-1]:
  print("Yes")
else:
  print("No")
