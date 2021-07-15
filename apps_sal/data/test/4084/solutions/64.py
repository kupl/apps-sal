N,A,B = map(int,input().split())
div = N//(A+B)
rm = N%(A+B)
print(div*A+min(rm,A))
