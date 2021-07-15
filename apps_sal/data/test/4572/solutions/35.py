s=input()
res="None"
for i in range(ord("a"),ord("z")+1):
    if chr(i) not in s:
        res=chr(i)
        break
print(res)
