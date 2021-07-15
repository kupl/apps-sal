A,B,C,D =map(int,input().split())
if A+B == C+D:
    print("Balanced")
else:
    print(("Left","Right")[A+B <C+D])
