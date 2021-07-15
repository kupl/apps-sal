(n, p, k) = map(int, input().split())

rightArrow = ">>"
leftArrow = "<< "

s = ""
startingIndex = 0
endingIndex = 0

if(p - k <= 1):
    startingIndex = 1
else:
    startingIndex = p-k
    s += leftArrow

if(p+k >= n):
    endingIndex = n
else:
    endingIndex = p+k

for i in range(startingIndex, endingIndex + 1):
    if(i is p):
        s += "("+str(i)+") "
    else: 
        s += str(i) + " "
if(p+k < n):
    s += rightArrow
print(s)
