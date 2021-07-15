# -*- coding: utf-8 -*-

N,M = list(map(int, input().split()))
s_list = []
c_list = []
for i in range(M):
    s,c = list(map(int, input().split()))
    s_list.append(s)
    c_list.append(str(c))

if N==1:
    start = 0
    end = 10
else:
    start = int("1"+("0" * (N-1)))
    end = int("9"*N) + 1

if M==0:
    print(start)
    return

for val in range(start, end):
    val_str = list(str(val))
    cnt = 0
    for i in range(M):
        digit = s_list[i]-1
        if val_str[digit] == c_list[i]:
            cnt += 1
        else:
            break

        if cnt==M:
            print(val)
            return

print((-1)) 

