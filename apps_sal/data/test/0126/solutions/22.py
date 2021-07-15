n = int(input())
s = input()
fill = [[False for i in range(3)] for j in range(4)]
for i in s:
    if i == "0":
        j = 10
    else:
        j = ord(i)-ord('1') #0, 1, 2, 3... 8
    fill[j//3][j%3] = True
#for i in fill:
#    print(i)
top = fill[0][0] or fill[0][1] or fill[0][2]
bottom = fill[2][0] or fill[3][1] or fill[2][2]
left = fill[0][0] or fill[1][0] or fill[2][0]
right = fill[0][2] or fill[1][2] or fill[2][2]
#print(left, right, fill[3][1], (not left or not right)and not fill[3][1])
if ((not left or not right)and not fill[3][1]) or not top or not bottom:
    print("NO")
else:
    print("YES")

