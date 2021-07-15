import sys,math
isprime = [0]*1000010
all_prime = [2]
next_prime = [0]*1000010
def seive():
    isprime[1] = isprime[0] = 1
    limit = int(math.sqrt(1000010))+2
    for i in range(4,1000010,2):
        isprime[i] = 1
    for i in range(3,1000010,2):
        if(not isprime[i]):
            all_prime.append(i)
            if(i <= limit):
                for j in range(i*i,1000010,i*2):
                    isprime[j] = 1
seive()
prime = 0
for i in range(1000000):
    next_prime[i] = all_prime[prime]
    if(all_prime[prime] == i):
        prime+=1
r,c = map(int,input().split())
input_matrix = []
move = []
for i in range(r):
    temp = list(map(int,input().split()))
    input_matrix.append(temp)
for i in range(r):
    co = 0
    for j in range(c):
        co+= next_prime[input_matrix[i][j]] - input_matrix[i][j]
    move.append(co)
for i in range(c):
    co = 0
    for j in range(r):
        co+= next_prime[input_matrix[j][i]] - input_matrix[j][i]
    move.append(co)
print(min(move))
