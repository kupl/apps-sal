N , X , T = map(int,input().split())
if  (N % X) == 0:
    times = N // X
else:
    times = N // X + 1
print(T * times)
