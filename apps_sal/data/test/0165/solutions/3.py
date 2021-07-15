b,d,s = list(map(int, input().split()))

r = 0
if b == s and d == s:
    print(0)
elif b >= s and b >= d:
    print(max(0,abs(b-d)-1)+max(abs(b-s)-1,0))
elif s >= b and s >= d:
    print(max(0,abs(s-b)-1)+max(abs(s-d)-1,0))
elif d >= s and d >= b:
    print(max(0,abs(d-s)-1)+max(abs(d-b)-1,0))
    

