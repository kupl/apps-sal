n = int(input())
seq = []
x = 1
for i in range(n//2):
    s = 'D' * x
    star = (n - x) // 2
    s = '*' * star + s + '*' * star
    x += 2
    seq.append(s)


for i in range(0,len(seq)):
    print(seq[i])
print('D'*n)

for i in range(len(seq)-1,-1,-1):
    print(seq[i])
    
    
    

