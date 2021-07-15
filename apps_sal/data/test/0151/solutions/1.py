string = input()
def sogl(ch):
    if ch!='a' and ch!='e' and ch!='i' and ch!='o' and ch!='u':
        return True
    return False
fast = 0
for i in range(len(string)):
    if(fast>0):
        fast-=1
        continue
    if i<len(string)-2 and( not (string[i]==string[i+1] and string[i]==string[i+2])) and sogl(string[i]) and sogl(string[i+1]) and sogl(string[i+2]):
        print(string[i]+string[i+1]+' ',end='')
        fast = 1
        continue
    print(string[i],end='')

