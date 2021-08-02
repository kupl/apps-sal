def getMoves(arr, num, k):
    count = 0
    n = len(arr)
    total_moves = 0
    for i in range(n):
        moves = 0
        curr = arr[i]
        while True:
            if curr <= num:
                break
            moves += 1
            curr = curr // 2

        if curr == num:
            total_moves += moves
            count += 1

        if count >= k:
            break

    # print(total_moves,num,count)
    if count >= k:
        return total_moves

    return float('inf')


def main():
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    min_moves = float('inf')
    arr.sort()
    for i in range(2 * 10**5 + 1):
        moves = getMoves(arr, i, k)
        min_moves = min(min_moves, moves)

    print(min_moves)


main()
