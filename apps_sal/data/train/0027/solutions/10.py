t = int(input())



for _ in range(t):
    used_q = set()
    n = int(input())
    nums = list(map(int,input().split(' ')))
    for i in range(len(nums)):
        q = nums[i]
        while q % 2 == 0:
            if q in used_q:
                q = q // 2
            else:
                used_q.add(q)
                q = q // 2
    print(len(used_q))



