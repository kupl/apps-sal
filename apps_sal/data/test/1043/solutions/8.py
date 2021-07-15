from math import log2, floor

def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)


def next_two_pow(val):
    pw=0
    while 2**pw <= val:
        pw=+1
    return pw        

n = int(input())
arr=[int(x) for x in input().split()]


win_idx =-1
selected=[]

for i in range(1,n+1):
    val = arr[i-1]
    if win_idx ==-1:
       if  val == -1: 
           win_idx =i
    else:
         if is_power2(i):
             selected.append(val)
             selected.sort()
         else:
             if len(selected) > 0 and val < selected[-1]:
                 selected.pop()
                 selected.append(val)
                 selected.sort()

print(sum(selected))


# if arr[n-1] ==-1:
#     print(0)
# else:
#     win_idx =-1
#     for i in range(0,n):
#         if arr[i] == -1:
#             win_idx =i
#             break
# 
#     crt_pow=int(floor(log2(n)))
#     stop_pow=next_two_pow(win_idx)
#     total=0
#     taken= set()
#     while crt_pow > stop_pow:
#         two_p = 2**crt_pow
#         mn = 10**9 + 1
#         mn_idx = -1
#         for i in range(two_p - 1, n):
#             if i!=win_idx and i not in taken and  arr[i] < mn:
#                 mn =arr[i]
#                 mn_idx=i
#         crt_pow -=1        
#         taken.add(mn_idx)
#         total+=mn
#     print(total)    

