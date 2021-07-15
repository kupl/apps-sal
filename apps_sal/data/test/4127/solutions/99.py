
M, N = input().split()   # 2つ整数の読み取り
A=int(M)
B=N.replace(".","")
B=int(B)

C=A*B//100
print(C)
