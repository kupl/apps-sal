N,A,B = list(map(int, input().split()))
M = N%(A+B)
ans = N//(A+B)
print(ans*A + A) if M >= A else print(ans*A + M)
