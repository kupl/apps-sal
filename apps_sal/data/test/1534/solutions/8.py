s=input()
                        #________b..._________
back=0                  #itung a sampe ktemu b [a....]
now=0                   #setelah a../nggak, jumlah b [a...b.. / b...]
after_ab=0              #setelah a..b.. [a..b..a]
for i in s:
    if i=='a':
        back+=1
        after_ab=max(after_ab,now)+1
    else:
        now=max(back,now)+1
print(max(back,max(now,after_ab)))
        
        

