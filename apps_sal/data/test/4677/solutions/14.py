s=input()
output=''
for i in s:
    if i!='B':
        output+=i
    elif i=='B':
        output=output[:-1]
print(output)

