def main():
    n = int(input())
    nums = list(map(int, input().split()))
    odd = []
    even = []
    
    for ni in nums:
        if ni % 2 == 0:
            even.append(ni)
        else:
            odd.append(ni)
            
    if len(odd) == 0 or len(even) == 0:
        print(' '.join(map(str, nums)))
        return 0

    nums.sort()
    print(' '.join(map(str, nums)))
    return 0
    
main()
