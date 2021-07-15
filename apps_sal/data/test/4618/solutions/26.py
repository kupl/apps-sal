s = list(input())
k =  int(input())
s.append((''))
Dict = {}
dict_keys = []
for left in range(len(s)):
    for right in range(left+1,len(s)):
        string = ''.join(s[left:right])
        if len(string)>k:
            break
        if string not in Dict.keys():
            Dict[string] = True
Dict = sorted(Dict.keys())
print(Dict[k-1])
