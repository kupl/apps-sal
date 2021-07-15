for h in range(int(input())):
    n, k, l = list(map(int, input().strip().split()))
    
    arr = list(map(int, input().strip().split()))
    
    
    dp = [0 for i in range(len(arr)+1)]
    dp[0] = -1
    
    # print(p)
    
    there = True
    
    for i in range(len(arr)):
        if arr[i] > l:
            there = False
            break
        elif arr[i]+k > l:
            dp[i+1] = arr[i]
        else:
            dp[i+1] = -1
    
    if there == False:
        print("No")
        continue
    pointer = 0
    
    for i in range(n+1):
        if dp[i] == -1:
            if i == n:
                continue
            elif i < n:
                maxi = l-dp[i+1]
                pointer = -maxi-1
        else:
            pointer += 1
            if dp[i] + abs(pointer) > l:
                if pointer >= 0:
                    there = False
                    break
                else:
                    pointer = -(l-dp[i])
    
    if there == False:
        print("No")
    else:
        print("Yes")
            
    
    
    

