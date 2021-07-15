a,b=map(int, input().split())
s=input()
res="No"
if s[a]=="-":
    if s[:a].isdecimal() and s[a+1:].isdecimal():
        res="Yes"
print(res)
