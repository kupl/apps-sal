def solve(a,b,groups,nums,visited):
    group1 = set(nums[a])
    group2 = set(nums[b])
    common = group1&group2
    for i in common:
        if i not in visited:
            group = i

    #print(group)
    visited.add(group)
    for i in groups[group]:
        if i != a and i != b:
            return i
    

def main():
    n = int(input())
    nums = {}
    ans = []
    groups = []
    for i in range(n-2):
        arr = list(map(int,input().split()))
        for j in arr:
            if j not in nums.keys():
                nums[j] = [i]
            else:
                nums[j].append(i)

        groups.append(arr)

    first = -1
    for i in nums.keys():
        if len(nums[i]) == 1:
            first = i
            break

    visited = set()
    ans.append(first)
    group = nums[first][0]
    for i in groups[group]:
        if len(nums[i]) == 2:
            second = i
            break
        
    ans.append(second)
    for i in groups[group]:
        if i not in ans:
            ans.append(i)
            break

    visited.add(group)
    a = ans[-2]
    b = ans[-1]
    for i in range(n-3):
        ans.append(solve(a,b,groups,nums,visited))
        a = ans[-2]
        b = ans[-1]

    for i in ans:
        print(i,end = ' ')
    

main()

