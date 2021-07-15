A,B=map(int,input().split())
print((sorted(({((int(i*0.08)==A)&(int(i*0.1)==B))*i for i in range(10*B+10)}))+[-1])[1])
