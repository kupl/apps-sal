n = int(input())
n = bin(n)[2:]
n = "0"*(6-len(n))+n

s = n[0] + n[5] + n[3] + n[2] + n[4] + n[1]
print(int(s,2))
