n = int(input())
count1, count2 = 0, 0
for i in range(n):
    a, b = map(int, input().split())
    if(a > b):
        count1 += 1
    elif(a < b):
        count2 += 1
if(count1 == count2):
    print("Friendship is magic!^^")
elif(count1 > count2):
    print("Mishka")
else:
    print("Chris")
