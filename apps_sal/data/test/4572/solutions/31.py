s = input()
s = set(s)
data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(data)):
    if data[i] not in s:
        print(data[i])
        break
else:
     print('None')   
