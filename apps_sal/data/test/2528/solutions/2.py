# cook your dish here
n=int(input())
arr=[int(x) for x in input().split()]
# arr.append(0)
subarr=[]
prev=[]
if 0 in arr:
 for val in range(len(arr)):
  if arr[val]==0:
   if len(subarr)>len(prev):
    prev=subarr
   subarr=[]
   
  else:
   subarr.append(arr[val])
 # print(subarr,prev)
 print(max(len(prev),len(subarr)))
else:
 print(n)
  


# maxy=[]
# ans=1
# pre_ans=0
# if 0 in arr:
#     for val in range(len(arr)):
#         if arr[val]!=0:
#             ans=ans*arr[val]
#             maxy.append(arr[val])
#         else:
#             if ans>pre_ans:
#                 final=maxy
#             pre_ans=ans
#             maxy=[]
#             ans=1
#     print(len(final))
# else:
#     print(n)

