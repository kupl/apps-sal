import math

n = int(input())

def get(n):
    temp = (math.sqrt(8*(n+1)+1)-1)/2
    # print("Inside",8*(n+1)+1)
    # print("before /2",math.sqrt(8*(n+1)+1)-1)
    # print("temp",temp)
    return math.floor(temp)

def check(n):
    target = get(n)
    if (((target+1)*(target+2)//2) <= (n+1)):
        return target+1
    elif ((target*(target+1)//2) <= (n+1)):
        return target
    elif (((target-1)*target//2) <= (n+1)):
        return target-1

# print("get",get(n))
# print("check",check(n))
print(n+1-check(n))
