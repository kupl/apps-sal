A,B,T = map(int,input().split())
time = A
cnt = 0
while time < T + 0.5:
    time += A 
    cnt += B 
print(cnt)
