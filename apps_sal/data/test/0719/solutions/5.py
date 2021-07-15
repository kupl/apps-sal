nums = set()

def generate(missing, num):
    if int(num) > 10**8:
        return
    if missing == 0:
        nums.add(int(num))
    for k in range(missing + 1):
        generate(missing - k, num + str(k))

for i in range(1, 10):
    generate(10-i, str(i))

nums2 = list(nums)
nums2.sort()

k = int(input())

print(nums2[k-1])


        

