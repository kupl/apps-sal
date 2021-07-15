def main():
    n, k = list(map(int, input().split()))
    nums = input().split()

    nums.append('0')
    n += 1
    maxr = maxi = front = rear = 0
    while front < n:
        for front in range(front, n):
            if nums[front] == '0':
                if k > 0:
                    k -= 1
                else:
                    break

        r = front - rear
        if r > maxr:
            maxr = r
            maxi = rear

        if nums[rear] == '0':
            if front > rear:
                k += 1
            else:
                front += 1
        rear += 1

    nums.pop()
    nums[maxi:maxi+maxr] = ('1' for _ in range(maxr))
    print(maxr)
    print(' '.join(nums))

main()

