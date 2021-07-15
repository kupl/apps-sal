def main():
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    nums = [[0 for i in range(2)] for j in range(2*10**5+1)]
    arr.sort()
    for i in arr:
        moves = 0
        #print('start')
        while i >= 0:
            if nums[i][0] == k:
                break
            nums[i][0] += 1
            nums[i][1] += moves
            moves += 1
            i = i//2
            if i == 0:
                nums[i][0] += 1
                nums[i][1] += moves
                break

    min_moves = float('inf')
    for i in range(2*10**5+1):
        if nums[i][0] >= k:
            min_moves = min(min_moves,nums[i][1])

    print(min_moves)


main()

