
def get_bin (a):
    nums=[]
    for i in range (32):
        if ((1<<i)&a):
            nums.append(1)
        else:
            nums.append(0)
    
    while(len(nums)>0 and nums[-1]==0):
        nums.pop()
    
    return nums

dp={}
def get_num (a, b):
    nonlocal dp
    if ((a,b) in dp):
        return dp[(a,b)]
    if (a < 0 or b < 0):
        return 0 
    if (a == 0 and b == 0):
        return 1
    
    a_bin = get_bin(a)
    b_bin = get_bin(b)
    
    if(b>a):
        a_bin,b_bin=b_bin,a_bin
        a,b=b,a
    
    if (len(a_bin)>len(b_bin)):
        big_bit = 1 << (len(a_bin) - 1)
        to_ret=((get_num(big_bit-1,b) + get_num(a-big_bit, b)))
        dp[(a,b)]=to_ret
        return to_ret
    
    if(sum(a_bin)==len(a_bin) and sum(b_bin)==len(b_bin)):
        to_ret = pow(3, len(a_bin))
        dp[(a,b)]=to_ret
        return to_ret
        
    big_bit = 1 << (len(a_bin) - 1)
    to_ret=(get_num(big_bit-1, b-big_bit) + get_num(a, big_bit-1))
    dp[(a,b)]=to_ret
    return to_ret
    
    
        
    
tc = int(input(""))

for i in range (int(tc)): 
    nums = input("").split(' ')
    
    l = int(nums[0])
    r = int(nums[1])
    
    ans = get_num(r, r) - 2 * get_num(r, l - 1) + get_num(l - 1, l - 1)

    print(ans)

