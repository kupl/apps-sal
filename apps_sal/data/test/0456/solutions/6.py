n = int(input())

s = input()

save = ''
i = 0
ny = ''
while i<n:
    if save=='':
        if s[i:i+3]=='ogo':
            save = 'o'
            i+=2
        else:
            ny+=s[i]
    else:
        if s[i:i+2]=='go':
            i+=1
        else:
            save = ''
            ny+='***'
            i-=1
    i+=1
if save!='':
    ny+='***'
print(ny)
