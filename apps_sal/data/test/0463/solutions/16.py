[n,x] = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]


def foo():
    nonlocal x,n,nums
    a_plain = set()
    
    for i in range(n):
        if nums[i] not in a_plain:
            a_plain.add(nums[i])
        else:
            print(0)
            return

    for i in range(n):
        if (nums[i] & x) in a_plain and (nums[i] & x != nums[i]):
            print(1)
            return
    
    a_and = {}
    for i in range(n):
        temp = nums[i] & x
        if temp not in a_and:
            a_and[temp] = 1
        else:
            a_and[temp] += 1
    
    for k in a_and:
        if a_and[k] > 1:
            print(2)
            return
    print(-1)
        

foo()
