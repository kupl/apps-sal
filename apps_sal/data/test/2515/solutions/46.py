NUM = 10**5
prime = [True]*(NUM+1)
for i in range(2, int(NUM**0.5)+1):
    if not prime[i]:
        continue
    j = i*2
    while j <= NUM:
        prime[j] = False
        j += i

S = [0]*(NUM+1)
for i in range(3, NUM+1, 2):
    if prime[(i+1)//2] and prime[i]:
        S[i] = S[i-2] + 1
    else:
        S[i] = S[i-2]

Q = int(input())
for _ in range(Q):
    l, r = list(map(int, input().split()))
    print((S[r]-S[l-2]))


