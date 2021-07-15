n = int(input())
t = input()
if t == "1":
    print((10**10*2))
elif t == "0":
    print((10**10))
elif t == "11" or t =="10":
    print((10**10))
elif t == "01":
    print((10**10-1))
elif t == "110":
    print((10**10))
elif t == "101" or t == "011":
    print((10**10-1))
    
elif "00" in t or "010" in t or "111" in t:
    print((0))
    
elif t[0:2]=="11" and n%3==0:
    print((10**10-n//3+1))
elif t[0:2]=="01" and n%3==2:
    print((10**10-n//3-1))
else:
    print((10**10-n//3))


