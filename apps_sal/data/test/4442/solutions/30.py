a,b = map(int,input().split())

#整数同士のただの計算になってしまうため、型を指定する。
A = str(a) * b
B = str(b) * a

if a > b:
    print(B)
else:
    print(A)
