num2alpha = lambda c: chr(c+64)


N = int(input())
degit = 0
temp_degit = 0
top=0

for i in range(1,50):
    temp_degit += 1
    under = top+1
    top += 26**i
    # print(temp_degit)
    # print(under,top)
    if under <= N and N <= top:
        degit = temp_degit
# print(degit)

# print(N%26)
arr =[]
for i in range(degit):
    if N%26==0:
        arr.append(26)
        N -=1
    else:  
        arr.append(N%26)
    N//=26
    # print(N)

rsl=""
# print(arr)
# print(num2alpha(10))
for i in reversed(arr):
    rsl += num2alpha(i)
print(rsl.lower())
