N=int(input())
nums=[]
for i in range(N):
    A=int(input())
    nums.append(A)
    
nums2=sorted(nums,reverse=True)

for i in nums:
    if i==nums2[0]:
        print(nums2[1])
    else:
        print(nums2[0])
