S=input()
start=len(S)%2
if S[0]==S[-1]:
    goal=1
else:
    goal=0
can=(start+goal)%2
if can==0:
    print("Second")
else:
    print("First")
