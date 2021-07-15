s=input("")
list_s=list(s)
price=700
mylist=["o"]
for i in range(0,len(list_s)):
    if(list_s[i] in mylist):
        price+=100
    else:
        price+=0

print(price)
