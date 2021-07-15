n = int(input())

prime_1 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
prime_2 = [4,9,25,49]
prime_3 = [8,27]
prime_4 = [16,81]

dp = [0]*15

for i in range(15):
    dp[i] += n // prime_1[i]

for j in range(4):
    dp[j] += n // prime_2[j]
    
for k in range(2):
    dp[k] += n // prime_3[k]

for l in range(2):
    dp[l] += n // prime_4[l]

dp[0] += n // 32
dp[0] += n // 64

n2 = sum(x>1 for x in dp) 
n4 =sum(x>3 for x in dp)
n14=sum(x>13 for x in dp)
n24=sum(x>23 for x in dp)
n74=sum(x>73 for x in dp)

p553 = (n2-n4) * (n4*(n4-1) //2 ) + ((n4*(n4-1)*(n4-2))//2)
p144 = (n4-n14) * n14 + (n14*(n14-1))
p242 = (n2-n24) * n24 + (n24*(n24-1))
p750 = n74

print(p553+p144+p242+p750)
