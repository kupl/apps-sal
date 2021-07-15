S = input()
K = int(input())

cnt_one = 0
for i in S:
    if i == '1':
        cnt_one += 1
    else:
        break

if cnt_one >= K:
    print(1)
else:
    print(S[cnt_one+1-1])
