# coding: utf-8
# Your code here!




def insert_str(target, i, char):
    return target[:i] + char + target[i:]

def calc(target, i):
    nonlocal ans
    
    if ans != "":
        return
    
    if i == 7:
        if eval(target) == 7:
            ans = target+"=7"
            return ans
        return
    calc(insert_str(target, i, "+"), i+2)
    calc(insert_str(target, i, "-"), i+2)
        
S = input()
N = len(S)
ans = ""
calc(S, 1)


print(ans)





