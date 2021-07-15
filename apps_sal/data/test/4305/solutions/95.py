H,A = map(int,input().split())

cnt = 0
while(True) :
    H = H - A
    cnt += 1
    if H  <= 0 :
        break

print(cnt)
