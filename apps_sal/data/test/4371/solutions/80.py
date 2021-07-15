S = input()
N = len(S)
ans = 1000

for i in range(N-2):
    ans = min(ans, abs(753-(int(S[i])*100+int(S[i+1])*10+int(S[i+2]))))

print(ans)
