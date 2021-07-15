n=(input())
cur=int(n[0])
pre=str(cur+1)
next=pre+'0'*(len(n)-1)
print(int(next)-int(n))

