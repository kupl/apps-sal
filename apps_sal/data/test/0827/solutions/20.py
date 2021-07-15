N = int(input())
T = str(input())

mozi = "110" * (N//3+2)

a = mozi.find(T)

if a == -1:
    print(0)
elif T == "1":
    print(10**10*2)
else:
    print(10**10-int((a+N-1)/3))
