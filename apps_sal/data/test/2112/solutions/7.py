def subsequence(arr1,arr2,n,m):
    i = 0
    j = 0
    common = []
    while i < n and j < m:
        if arr1[i] == arr2[j]:
            common.append(i)
            j += 1
        i += 1

    if j == m:
        return common

    return []

def find(arr,start,end,x,y,k):
    stack = []
    second_use_limit = 0
    for i in range(start,end+1):
        if not stack:
            stack.append(arr[i])
        else:
            while stack and arr[i] > stack[-1]:
                second_use_limit += 1
                stack.pop()

            if (not stack) or (arr[i] > stack[-1]):
                stack.append(arr[i])
            elif stack and arr[i] < stack[-1]:
                second_use_limit += 1

    while stack and start-1 >= 0 and arr[start-1] > stack[0]:
        stack.pop(0)
        second_use_limit += 1

    while stack and end+1 < len(arr) and arr[end+1] > stack[-1]:
        stack.pop()
        second_use_limit += 1
    
    min_cost = float('inf')
    total = end-start+1
    #print(total,start,end)

    #print('here',x,y,k)
    i = 0
    while i*k <= total:
        rem = total-i*k
        if rem <= second_use_limit:
            #print(i*x+rem*y,i,rem)
            min_cost = min(min_cost,i*x+rem*y)

        i += 1

    if min_cost == float('inf'):
        return -1

    return min_cost

def main():
    n,m = list(map(int,input().split()))
    x,k,y = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    common = subsequence(arr1,arr2,n,m)
    if not common:
        print(-1)
        return

    cost = 0
    for i in range(len(common)):
        if i == 0:
            if common[i] > 0:
                start = 0
                end = common[i]-1
                if end >= start:
                    curr_cost = find(arr1,start,end,x,y,k)
                    if curr_cost == -1:
                        cost = -1
                        break

                    cost += curr_cost
            
        start = common[i]+1
        if i+1 < len(common):
            end = common[i+1]-1
        else:
            end = n-1

        if end >= start:
            curr_cost = find(arr1,start,end,x,y,k)
            if curr_cost == -1:
                cost = -1
                break

            cost += curr_cost

    print(cost)

main()

