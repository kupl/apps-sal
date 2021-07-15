n = int(input())

tmp = n
ans = []

while tmp >= 1:
    tmp -= 1
    #print(tmp,tmp%26)
    ans.append(chr(ord("a")+tmp % 26))
    tmp //= 26
    
print(*ans[::-1],sep="")
