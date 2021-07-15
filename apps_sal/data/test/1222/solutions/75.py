k = int(input())
nums = [1,2,3,4,5,6,7,8,9]
cnt = 1

for num in nums:
    if cnt == k:
        print(num)
        return
    else:
        if num%10 == 0:
            nums.append(num*10)
            nums.append(num*10+1)
        elif num%10 == 9:
            nums.append(num*10+8)
            nums.append(num*10+9)
        else:
            nums.append(num*10+num%10-1)
            nums.append(num*10+num%10)
            nums.append(num*10+num%10+1)
    cnt += 1


