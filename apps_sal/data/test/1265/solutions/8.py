str1 = input()
str2 = input()

if len(str1) != len(str2):
    print("NO")
    
else:
    if ('1' in str1) ^ ('1' in str2):
        print("NO")
    else:
        print("YES")

