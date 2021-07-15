N = int(input())
S = input()

cnt = 1
color = S[0]
for i in range(N-1):
    if S[i+1] != color:
        cnt += 1
    color = S[i+1]
print(cnt)
