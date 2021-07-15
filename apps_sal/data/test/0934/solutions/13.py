A = input()
n = input().split()
print('YES'if any(A.find(k[0])!=-1 or A.find(k[1])!=-1 for k in n)else'NO')

