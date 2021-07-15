N = int(input())
 
if N % 1000 == 0:
    print((0))
elif N < 1000:
    print((1000-N))
else:
    c = 1 + int(str(N)[0:len(str(N))-3])
    print((1000*c - N))

