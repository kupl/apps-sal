S = input()

mod = 10**9+7
A = 0
AB = 0
ABC = 0
cnt = 0
for i in range(len(S)):
    if S[i] == "A":
        A += pow(3, cnt, mod)
        A %= mod
    elif S[i] == "B":
        AB += A
        AB %= mod
    elif S[i] == "C":
        ABC += AB
        ABC %= mod
    else:
        ABC = (3*ABC + AB) % mod
        AB = (3*AB + A) % mod
        A = (3*A + pow(3, cnt, mod)) % mod
        cnt += 1
        
        
print(ABC)
