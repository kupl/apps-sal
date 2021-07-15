n = int(input())
inp = []
for i in range(n):
    inp1,inp2 = input().split(" ")
    inp.append([int(inp1),1]), inp.append([int(inp2),2])

result1,result2,result3 = "","",""
j = 0
inp.sort()
inpSort = inp
# k = 0

for i in inpSort:
    if j == n: break
    if i[1] == 1: result1 += "1"
    else : result2 += "1"
    j+=1
# k = n//2

for i in range(n//2):
    result3 += "1"

if len(result1) > len(result3):
    for i in range(n-len(result1)):
        result1+="0"
    for i in range(n-len(result3)):
        result3+="0"
    result = result1 + "\n" + result3
elif len(result2) > len(result3):
    for i in range(n-len(result2)):
        result2+="0"
    for i in range(n-len(result3)):
        result3+="0"
    result = result3 + "\n" + result2
else:
    for i in range(n-len(result3)):
        result3+="0"
    result = result3 + "\n" + result3

print(result)
