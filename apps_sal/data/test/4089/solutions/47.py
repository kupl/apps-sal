N = int(input())

ans = ' '
while N>0:
    N -= 1
    ans += chr(ord('a')+N%26)
    N = int(N/26)
    
print(ans[::-1])
