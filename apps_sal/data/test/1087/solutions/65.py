n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

B = [[0]*2 for _ in range(42)]
for a in A:
    b = format(a, 'b')
    b = list(b)
    b.reverse()
    for i in range(len(b)):
        if b[i] == '1':
            B[i][1] += 1

for i in range(42):
    if B[i][1] != 0:
        B[i][0] = n-B[i][1]
B.reverse()
#print(B)
temp = 0
max_ = 0
for i, (b0, b1) in enumerate(B):
    if b1 == 0:
        if temp + 2**(41-i) <= k:
            max_ += n*2**(41-i)
            temp += 2**(41-i)
    else:
        if b0 >= b1:
            if temp + 2**(41-i) <= k:
                max_ += b0*2**(41-i)
                temp += 2**(41-i)
            else:
                max_ += b1*2**(41-i)
                temp += 0
        else:
            max_ += b1*2**(41-i)
            temp += 0
print(max_)

