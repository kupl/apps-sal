def check(n, list1): 
    new = [] 
    for i in range(n): 
        new.append(list1[i]) 
          
    new.sort()
    swaps = 0
    for i in range(n): 
        if list1[i] != new[i]: 
            swaps += 1
              
    if swaps == 0 or swaps == 2: 
        return True
    else: 
        return False
  
n = int(input())

numbers =list(map(int, input().split()[:n]))



if check(n, numbers): 
    print("YES")
else:
    print("NO") 

      

