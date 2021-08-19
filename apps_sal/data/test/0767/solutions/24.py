n, z = input().split()
n = int(n)
z = int(z)
nums = list(map(int, input().split()))
nums.sort()
l1 = nums[:n // 2]
l2 = nums[n // 2:]
count = 0
ptr1 = 0
ptr2 = 0
while(ptr2 < len(l2) and ptr1 < len(l1)):
    # print(l2[ptr2]-l1[ptr1])
    # print(z)
    if((l2[ptr2] - l1[ptr1]) >= z):
        count += 1
        ptr1 += 1
        ptr2 += 1
    else:
        ptr2 += 1
print(count)
