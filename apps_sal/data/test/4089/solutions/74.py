a = int(input())
S =""
l =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = a % 26
while a >0:
    if a%26 !=0:
        S =l[(a%26)-1] + S
        a = (a-a%26)//26
    else:
        S = l[(a%26)-1] + S
        a = (a-26)//26
print(S)


