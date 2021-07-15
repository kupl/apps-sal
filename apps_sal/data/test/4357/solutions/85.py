A,B,C = input().split()
ls = [int(A+B)+int(C),int(B+A)+int(C),int(A)+int(B+C),int(A)+int(C+B),int(B)+int(A+C),int(B)+int(C+A)]
print(max(ls))
