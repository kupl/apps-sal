n=int(input())
s=input()
ic=s.count('I')
print(1 if ic==1 else 0 if ic>1 else s.count('A'))

